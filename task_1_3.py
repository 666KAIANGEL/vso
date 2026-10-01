import geometry
from geometry.flat import triangle_area
from geometry.solid import sphere_volume
from geometry.solid import hemisphere_area

print(geometry.__version__)
print(round(geometry.circle_area(3), 4))
print(triangle_area(6, 4))
print(round(sphere_volume(3), 4))
print(round(hemisphere_area(3), 4))
print(geometry.__all__)
print(geometry.__file__)

