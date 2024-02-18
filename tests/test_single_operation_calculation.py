from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.mathoperations import sqrt

@pytest.mark.parametrize("a, operation, expected", [
    (Decimal('25'), sqrt, Decimal('5')),
    (Decimal('100'), sqrt, Decimal('10.0'))
])

def test_calculation_single_operations(a, operation, expected):
    calc = Calculation(a = Decimal(a), singleOperation = operation)
    assert calc.perform_single() == expected, f"Failed {operation.__name__} operation with {a}"
        
def test_single_calculation_repr():
    calc = Calculation(a = Decimal('100'), singleOperation = sqrt)
    expected_repr = "Calculation(100, sqrt)"
    assert calc.repr() == expected_repr, "The repr method output does not match the expected string."