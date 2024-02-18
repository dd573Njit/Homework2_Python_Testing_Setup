import math
from decimal import Decimal
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sqrt(a: Decimal) -> Decimal:
    if a < 0:
        raise ValueError("Number cannot be negative")
    return Decimal(math.sqrt(float(a)))