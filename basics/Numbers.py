# Python Numbers Examples

# Integers
age = 25
count = -10
big_number = 1000000
print(f"Integer examples: {age}, {count}, {big_number}")

# Floats
price = 19.99
temperature = -5.5
pi = 3.14159
print(f"Float examples: {price}, {temperature}, {pi}")

# Arithmetic operations
x = 20
y = 3

add = x + y
subtract = x - y
multiply = x * y
divide = x / y  # always returns float
floor_divide = x // y  # returns integer
modulo = x % y  # remainder
power = x ** y

print(f"Addition: {x} + {y} = {add}")
print(f"Subtraction: {x} - {y} = {subtract}")
print(f"Multiplication: {x} * {y} = {multiply}")
print(f"Division: {x} / {y} = {divide}")
print(f"Floor Division: {x} // {y} = {floor_divide}")
print(f"Modulo: {x} % {y} = {modulo}")
print(f"Power: {x} ** {y} = {power}")

# Type conversion
str_num = "42"
int_from_str = int(str_num)
float_from_str = float(str_num)
int_to_float = float(25)
float_to_int = int(3.99)  # truncates decimal

print(f"String to int: {int_from_str} (type: {type(int_from_str).__name__})")
print(f"String to float: {float_from_str} (type: {type(float_from_str).__name__})")
print(f"Float to int: {float_to_int}")

# Math operations with built-in functions
import math

print(f"Absolute value of -15: {abs(-15)}")
print(f"Max of 10, 25, 5: {max(10, 25, 5)}")
print(f"Min of 10, 25, 5: {min(10, 25, 5)}")
print(f"Sum of [1, 2, 3, 4]: {sum([1, 2, 3, 4])}")
print(f"Round 3.7: {round(3.7)}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Power using math: {math.pow(2, 5)}")
print(f"Floor of 4.9: {math.floor(4.9)}")
print(f"Ceiling of 4.1: {math.ceil(4.1)}")

# Random numbers
import random

random_int = random.randint(1, 100)  # random integer from 1 to 100
random_float = random.random()  # random float between 0 and 1
random_choice = random.choice([10, 20, 30, 40])

print(f"Random integer (1-100): {random_int}")
print(f"Random float (0-1): {random_float}")
print(f"Random choice from list: {random_choice}")

# Number comparisons
a = 5
b = 10

print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} >= {b}: {a >= b}")

# Assignment operators
num = 10
num += 5  # num = num + 5
num -= 2  # num = num - 2
num *= 2  # num = num * 2
num /= 4  # num = num / 4
print(f"After operations: {num}")

# Number formatting
value = 123.456789
print(f"2 decimal places: {value:.2f}")
print(f"Scientific notation: {value:.2e}")
print(f"Percentage: {0.75:.1%}")
print(f"With thousand separator: {1000000:,}")
