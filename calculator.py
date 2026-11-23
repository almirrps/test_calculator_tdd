import math

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not possible")
    return a / b

def power(base: float, exponent: float) -> float:
    return base ** exponent

def square_root(n: float) -> float:
    if n < 0:
        raise ValueError("There is not real square root for a negative number")
    return math.sqrt(n)