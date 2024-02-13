from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.mathoperations import add, subtract, multiply, divide, sqrt

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('5'), Decimal('5'), add, Decimal('10')),
    (Decimal('25'), Decimal('5'), subtract, Decimal('20')),
    (Decimal('7'), Decimal('8'), multiply, Decimal('56')),
    (Decimal('49'), Decimal('7'), divide, Decimal('7')),
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),
])

def test_calculation_operations(a, b, operation, expected):
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"
    
def test_calculation_repr():
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.repr() == expected_repr, "The repr method output does not match the expected string."
    
def test_single_calculation_repr():
    calc = Calculation(a = Decimal('100'), singleOperation = sqrt)
    expected_repr = "Calculation(100, sqrt)"
    assert calc.repr() == expected_repr, "The repr method output does not match the expected string."

def test_divide_by_zero():
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()