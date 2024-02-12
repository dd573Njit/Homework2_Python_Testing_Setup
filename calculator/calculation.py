from typing import Callable
from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal = 0.0, b: Decimal = 0.0, operation: Callable[[Decimal, Decimal], Decimal] = None, singleOperation: Callable[[Decimal], Decimal] = None):
        self.a = a
        self.b = b
        self.operation = operation
        self.singleOperation = singleOperation
        
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal]], Decimal):
        return Calculation(a,b,operation)
    
    def _perform(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"