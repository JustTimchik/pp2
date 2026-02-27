import math

degree = 15
radian = math.radians(degree)
print("Radian:", round(radian, 6))

height = 5
base1 = 5
base2 = 6
trapezoid_area = 0.5 * (base1 + base2) * height  # Formula: 1/2 * (a+b) * h
print("Trapezoid area:", trapezoid_area)

n_sides = 4
side_length = 25
polygon_area = (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))
print("Polygon area:", polygon_area)

base = 5
height_parallelogram = 6
parallelogram_area = base * height_parallelogram  # Formula: base * height
print("Parallelogram area:", parallelogram_area)