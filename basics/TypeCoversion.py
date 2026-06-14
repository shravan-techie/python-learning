"""Type conversion examples and common patterns.

This module demonstrates safe conversions between `str`, `int`, `float`, and `bool`,
shows formatting and binary/hex conversions, and highlights precision issues and
the `Decimal` module for exact arithmetic.
"""

from decimal import Decimal
import math
import sys


def safe_int(value, default=None):
	"""Try to convert value to int, return default on failure."""
	try:
		return int(value)
	except (TypeError, ValueError):
		return default


def safe_float(value, default=None):
	"""Try to convert value to float, return default on failure."""
	try:
		return float(value)
	except (TypeError, ValueError):
		return default


def examples():
	# Basic conversions
	s = "42"
	f = "3.1415"
	print("String to int:", safe_int(s))
	print("String to float:", safe_float(f))

	# int/float to string
	n = 7
	pi = 3.14159
	print("Int to str:", str(n))
	print("Float to str:", str(pi))

	# float to int truncates (does not round)
	print("int(3.9) ->", int(3.9))

	# boolean conversions
	print("bool(0) ->", bool(0))
	print("bool(1) ->", bool(1))
	print("bool('') ->", bool(""))
	print("bool('False') ->", bool("False"))

	# numeric formatting
	value = 12345.6789
	print(f"Formatted (2 decimals): {value:.2f}")
	print("With thousand separator:", f"{int(1_000_000):,}")

	# binary / hex
	print("bin(10):", bin(10))
	print("hex(255):", hex(255))
	print("int('0b1010', 2):", int("0b1010", 2))

	# rounding and math utilities
	print("round(2.675, 2):", round(2.675, 2))
	print("math.floor(4.9):", math.floor(4.9))
	print("math.ceil(4.1):", math.ceil(4.1))

	# Decimal for exact arithmetic (money)
	a = Decimal('0.1')
	b = Decimal('0.2')
	print("Decimal 0.1 + 0.2 ->", a + b)
	print("Float 0.1 + 0.2 ->", 0.1 + 0.2)

	# safe parsing of user-like input (no interactive input required)
	samples = ['10', '3.5', 'abc', None]
	for item in samples:
		print(f"parse '{item}': int->{safe_int(item)}, float->{safe_float(item)}")


def interactive_demo():
	"""Run the original interactive snippet supplied by the user.

	This function asks for input and demonstrates types and falsy checks.
	It's optional: run the module with argument `interactive` to use it.
	"""
	try:
		number = int(input("enter a no "))
	except Exception as exc:
		print("Invalid input:", exc)
		return

	x = number + 2
	print(type(number))  # checking type of the input
	print(f"value of x: {x}, Value of number is: {number}")
	print(f"Type of x: {type(x)}, Type of number is: {type(number)}")

	# Falsy values (in boolean context)
	# ""
	# None
	# 0

	print(bool(0))
	print(bool(1))
	print(bool(""))
	print(bool())
	print(bool(False))
	print(bool(None))


if __name__ == "__main__":
	# Run interactive demo only when explicitly requested to avoid blocking
	if len(sys.argv) > 1 and sys.argv[1].lower() == "interactive":
		interactive_demo()
	else:
		examples()
