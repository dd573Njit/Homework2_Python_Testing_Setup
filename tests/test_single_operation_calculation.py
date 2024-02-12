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