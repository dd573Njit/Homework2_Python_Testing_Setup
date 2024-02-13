from typing import Callable
from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal = 0.0, b: Decimal = 0.0, operation: Callable[[Decimal, Decimal], Decimal] = None, singleOperation: Callable[[Decimal], Decimal] = None):
        self.a = a
        self.b = b
        self.operation = operation
        self.singleOperation = singleOperation
        
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        return Calculation(a,b,operation)
    
    @staticmethod
    def createForSingleOpr(a: Decimal, singleOperation: Callable[[Decimal], Decimal]):
        return Calculation(a = a, singleOperation = singleOperation)
    
    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    def perform_single(self) -> Decimal:
        return self.singleOperation(self.a)
    
    def repr(self):
        if self.operation is not None:
            operation_name = self.operation.__name__
            return f"Calculation({self.a}, {self.b}, {operation_name})"
        elif self.singleOperation is not None:
            operation_name = self.singleOperation.__name__
            return f"Calculation({self.a}, {operation_name})"
    
        