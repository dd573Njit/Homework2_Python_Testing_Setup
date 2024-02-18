from decimal import Decimal
from calculator.calculation import Calculation
from calculator.mathoperations import sqrt

def test_calculation_single_operations(a_num, operation, expected):
    calc = Calculation(a = Decimal(a_num), singleOperation = operation)
    assert calc.perform_single() == expected, f"Failed {operation.__name__} operation with {a_num}"
        
def test_single_calculation_repr():
    calc = Calculation(a = Decimal('100'), singleOperation = sqrt)
    expected_repr = "Calculation(100, sqrt)"
    assert calc.__repr__() == expected_repr, "The repr method output does not match the expected string."