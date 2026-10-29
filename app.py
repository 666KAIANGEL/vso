import pyautogui
import cv2
import numpy as np
from ultralytics import YOLO
import time
import os
import threading

MODEL_PATH = 'best.pt'

if not os.path.exists(MODEL_PATH):
    print(f"❌ Файл модели не найден: {MODEL_PATH}")
    exit()

print("✅ Модель найдена. Загрузка...")
model = YOLO(MODEL_PATH)
CLASS_NAMES = model.names

SCREEN_W, SCREEN_H = pyautogui.size()

# СУЖАЕМ ОБЛАСТЬ ПОИСКА
# Если кнопки появляются строго в центре, ставим 0.4 или 0.5. 
# Это отсечет ложные срабатывания по краям интерфейса.
ROI_W = int(SCREEN_W * 0.5)
ROI_H = int(SCREEN_H * 0.5)
ROI_X = (SCREEN_W - ROI_W) // 2
ROI_Y = (SCREEN_H - ROI_H) // 2

# Настройки анти-спама
last_click_time = 0
CLICK_COOLDOWN = 1.5  # Увеличили паузу между кликами до 1.5 сек (чтобы не дергалось)

# Защита от кликов по одному и тому же месту
last_click_pos = (0, 0)
POS_TOLERANCE = 50 # Если клик попадает в радиус 50px от прошлого - считаем это залипанием

is_paused = False

def listen_for_enter():
    global is_paused
    while True:
        try:
            input()
            is_paused = not is_paused
            print("\n⏸️ ПАУЗА. Нажмите Enter, чтобы продолжить..." if is_paused else "\n▶️ ПРОДОЛЖАЕМ РАБОТУ...")
        except EOFError:
            break

threading.Thread(target=listen_for_enter, daemon=True).start()

def find_and_click():
    global last_click_time, last_click_pos
    
    # Если на паузе или кулдаун не прошел
    if is_paused or (time.time() - last_click_time < CLICK_COOLDOWN):
        return False

    screenshot = pyautogui.screenshot(region=(ROI_X, ROI_Y, ROI_W, ROI_H))
    screenshot_np = np.array(screenshot)
    screenshot_np = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # УВЕЛИЧИВАЕМ ПОРОГ УВЕРЕННОСТИ ДО 0.85
    # Если модель ошибается, она обычно выдает conf 0.7-0.8. 
    # Настоящие кнопки обычно имеют conf 0.95+
    results = model(screenshot_np, verbose=False, conf=0.85)

    best_targets = {}

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = float(box.conf[0])
            cls_id = int(box.cls[0])
            class_name = CLASS_NAMES[cls_id]

            # Жесткие пороги
            required_conf = 0.90 if class_name == 'game' else 0.85
            if confidence < required_conf:
                continue

            real_x1 = x1 + ROI_X
            real_y1 = y1 + ROI_Y
            real_x2 = x2 + ROI_X
            real_y2 = y2 + ROI_Y

            center_x = (real_x1 + real_x2) / 2
            center_y = (real_y1 + real_y2) / 2

            if class_name not in best_targets or confidence > best_targets[class_name][0]:
                best_targets[class_name] = (confidence, center_x, center_y)

    acted = False
    
    if is_paused:
        return False

    target_to_click = None

    if 'upgrade' in best_targets:
        target_to_click = best_targets['upgrade']
        print_type = "⬆️ Улучшение"
    elif 'game' in best_targets:
        target_to_click = best_targets['game']
        print_type = "🎮 Игра"

    if target_to_click:
        conf, cx, cy = target_to_click
        
        # ПРОВЕРКА НА ЗАЛИПАНИЕ (Клик по тому же месту)
        dist = ((cx - last_click_pos[0])**2 + (cy - last_click_pos[1])**2)**0.5
        if dist < POS_TOLERANCE:
            print(f"⚠️ Пропуск клика: объект на том же месте ({cx:.0f}, {cy:.0f}). Ждем изменений...")
            # Принудительно ставим кулдаун, чтобы скрипт не спамил в консоль
            last_click_time = time.time()
            return False

        print(f"{print_type} (conf: {conf:.2f}) → клик по ({cx:.0f}, {cy:.0f})")
        pyautogui.click(cx, cy)
        
        last_click_time = time.time()
        last_click_pos = (cx, cy)
        acted = True

    return acted

print("🚀 Скрипт запущен.")
print("💡 Нажмите ENTER в этом окне, чтобы поставить на ПАУЗУ или ПРОДОЛЖИТЬ.")
print("💡 Мышка в углу экрана = экстренная остановка.")
print(f"📸 Область поиска: {ROI_W}x{ROI_H} в центре экрана.")

while True:
    try:
        if find_and_click():
            time.sleep(0.2)
        else:
            time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n🛑 Остановлено.")
        break
    except pyautogui.FailSafeException:
        print("\n🛑 FailSafe сработал (мышь в углу). Остановлено.")
        break
    except Exception as e:
        print(f"\n⚠️ Ошибка: {e}")
        time.sleep(1)