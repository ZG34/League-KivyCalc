import numbers


class CalculatorError(Exception):
    """An exception class for our calculator"""


class Calculator:
    """simple calculator."""

    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        return a + b

    def resists(self, dmg, resists):
        try:
            return round(int(dmg) / (1 + (int(resists) / 100)))
        except ValueError as e:
            return False

    def ehp(self, resists, health):
        try:
            return (1 + (int(resists) / 100)) * int(health)
        except ValueError as e:
            return False

    def _check_operand(self, operand):
        if not isinstance(
            operand, numbers.Number
        ):  # int/float/real etc all fall under Number
            raise CalculatorError(f"{operand} was not a number")

    def _converter(self, num):
        try:
            return float(num)
        except ValueError as e:
            raise CalculatorError(f"Conversion Error: {num} can not convert")

    def runner(self, *args, **kwargs):
        internal_calc = Calculator()
        operations = [
            internal_calc.add,
            internal_calc.resists,
            internal_calc.ehp,
        ]
        while True:
            print("Pick an operation")
            options = enumerate(operations, start=1)
            nums = []
            for i, operation in options:
                nums.append(str(i))
                print(f"{i}: {operation.__name__}")
            print("q: quit")
            operation = input("pick an operation: ")
            if operation == "q":
                return
            elif operation not in nums:
                print("\nERROR: please pick a listed number \n")
            else:
                op = int(operation)
                try:
                    a = internal_calc._converter(input("what is a?"))
                    b = internal_calc._converter(input("what is b?"))
                except CalculatorError as e:
                    print(f"CalculatorError: {e}")
                try:
                    print(operations[op - 1](a, b))
                except (CalculatorError, NameError) as e:
                    print(e)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.runner()
