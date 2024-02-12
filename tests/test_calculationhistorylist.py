from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculationhistorylist import CalculationHistoryList
from calculator.mathoperations import add, subtract, sqrt

@pytest.fixture
def setup_calculations():
    CalculationHistoryList.clear_history()
    CalculationHistoryList.store_calculation(Calculation(Decimal('111'), Decimal('5'), add))
    CalculationHistoryList.store_calculation(Calculation(a = Decimal('49'), singleOperation = sqrt))
    CalculationHistoryList.store_calculation(Calculation(Decimal('45'), Decimal('32'), subtract))

def test_store_calculation(setup_calculations):
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    CalculationHistoryList.store_calculation(calc)
    assert CalculationHistoryList.get_latest_calculation() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    history = CalculationHistoryList.get_history()
    assert len(history) == 3, "History does not contain the expected number of calculations"

def test_clear_history(setup_calculations):
    CalculationHistoryList.clear_history()
    assert len(CalculationHistoryList.get_history()) == 0, "History was not cleared"

def test_get_latest(setup_calculations):
    latest = CalculationHistoryList.get_latest_calculation()
    assert latest.a == Decimal('45') and latest.b == Decimal('32'), "Did not get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    add_operations = CalculationHistoryList.find_by_math_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = CalculationHistoryList.find_by_math_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    CalculationHistoryList.clear_history()
    assert CalculationHistoryList.get_latest_calculation() is None, "Expected None for latest calculation with empty history"