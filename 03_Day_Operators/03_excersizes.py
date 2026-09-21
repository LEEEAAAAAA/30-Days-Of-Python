import math

age = 18
my_height = 1.70

# This is a complex number in python
z = 3 + 4j
print(z)
print(type(z))
print(z.real)
# you can use .real or -imag to find the real and imaginary parts of the complex number
# z.real = 3
# z.imag = 4
# Explanation: Phase of complex number Geometrically, the phase of a complex number is the angle between the positive real axis and the vector representing a complex number. This is also known as the argument of a complex number.

base = float(input('Enter a number for the base: '))
height = float(input('Enter a number for the height: '))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

side_a = float(input('Enter a number for the side a: '))
side_b = float(input('Enter a number for the side b: '))
side_c = float(input('Enter a number for the side c: '))
perimeter = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter}")

rectangle_length =  float(input('Enter a number for the rectangle length: '))
rectangle_width = float(input('Enter a number for the rectangle width: '))
area = rectangle_length * rectangle_width
print(f"The area of the rectangle is {area}")
perimeter = 2 * (rectangle_length + rectangle_width)
print(f"The perimeter of the rectangle is {perimeter}")

radius = float(input('Enter a number for the radius: '))
circle_area = math.pi * radius * radius
print(f"The circle area of the rectangle is {circle_area}")
circumference = 2 * math.pi * radius
print(f"The circumference of the rectangle is {circumference}")


# Slope
# y = 2x - 2
# y = mx (+) b
m = 2
b = -2
x_intercept = -b / m

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1, y1 = 0, -2
x2, y2 = 4, 6
second_slope = (y2 - y1) / (x2 - x1)
print(f"The first slope is {slope}")
print(f"The second slope is {second_slope}")
difference = slope - second_slope
print(f"The difference is {difference}")

# y=x ^ 2 + 6
def calculate_y(x):
    return x**2 - 4*x +4

for x in range(-5, 6):
    y = calculate_y(x)
    print(f"x is {x}, y is {y}")

# A falsy comparison statement.
py_len = len("python")
dr_len = len("dragon")
print(py_len == dr_len)
print("on" in "python" and "on" in "dragon")

stringeling = "I hope this course is not full of jargon"
print("jargon" in stringeling)

print(not "on" in "python" and "on" in "dragon")

len_python = len("python")
py_as_float = float(len_python)
py_as_string = str(py_as_float)
print(py_as_string)

number = 9
if number % 2 == 0:
    print("even")
if number % 2 != 0:
    print("odd")
print("even" if number % 2 == 0 else "odd")

print(7 // 3 == int(2.7)) # Floor division

print(type("10") == type(10))
# print(int('9.8') == 10)  --> Schmeisst ValueError...


hours_per_month = int(input("Enter Hours: "))
income_per_month = int(input("Enter income per month: "))
print(income_per_month / hours_per_month)

years = int(input("Enter number of years you have lived: "))
lived = years * 365 * 24 * 60 * 60
will_live = (100 * 365 * 24 * 60 * 60 ) - lived
print(lived)
print(will_live)

for row in range(1, 6):
    for power in range(0, 5):
        print(row ** power, end=" ")
    print()
