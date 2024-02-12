from decimal import Decimal
from typing import Callable, List

from calculator.calculation import Calculation

class CalculationHistoryList:
    history: List[Calculation] = []

    @classmethod
    def store_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest_calculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None
    @classmethod
    def find_by_math_operation(cls, operation_name: str) -> List[Calculation]:
        return [calc for calc in cls.history if ((calc.operation and calc.operation.__name__ == operation_name) or (calc.singleOperation and calc.singleOperation.__name__ == operation_name)) and operation_name is not None]
    
