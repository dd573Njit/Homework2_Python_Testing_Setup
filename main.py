import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator  # Assuming Calculator is defined as shown previously

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b = None):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            if self.b is not None:
                return operation_method(self.a, self.b)
            else:
                return operation_method(self.a)  # Call unary operation with a single argument
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")


def calculate_and_print(a, b=None, operation_name=None):
    try:
        # Check if the operation is unary and prepare operands accordingly
        if operation_name == 'sqrt' and b is None:
            operands = [a]  # For unary operation, only 'a' is needed
            operation_display = f"{operation_name} {a}"
        else:
            operands = [a, b]  # For binary operations, both 'a' and 'b' are used
            operation_display = f"{a} {operation_name} {b}"
        
        # Convert operands to Decimal
        decimals = list(map(Decimal, operands))
        
        # Initialize and execute the operation command
        command = OperationCommand(Calculator, operation_name, *decimals)
        result = command.execute()
        
        print(f"The result of {operation_display} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    if len(sys.argv) not in [3, 4]:
        print("Usage: python calculator_main.py <number1> [<number2>] <operation>")
        sys.exit(1)
    
    if len(sys.argv) == 4:
        _, a, b, operation_name = sys.argv
        calculate_and_print(a, b, operation_name)
    else:
        _, a, operation_name = sys.argv
        calculate_and_print(a, operation_name=operation_name)


if __name__ == '__main__':
    main()