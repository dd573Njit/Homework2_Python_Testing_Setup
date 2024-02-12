from calculator.calculationhistorylist import CalculationHistoryList
from calculator.mathoperations import add, subtract, multiply, divide, sqrt
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable 
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        CalculationHistoryList.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)
    
    @staticmethod
    def sqrt(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, sqrt)