from math import pi
solid_cylinder_dia = 3
cylinder_radius = solid_cylinder_dia / 2
loss = 0.05
internal_radii = float(input("Enter the internal radius:"))
external_radii = float(input("Enter the external radius:"))
vol_of_sphere = 4/3 * pi * external_radii ** 3 - 4/3 * pi * internal_radii ** 3
height = (vol_of_sphere / pi * cylinder_radius * cylinder_radius)
print("height of the solid cylinder:",height)
