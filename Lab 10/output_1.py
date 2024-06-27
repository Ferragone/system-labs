class BasicCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    # Калькулятор не має методів для множення та ділення


class AdvancedCalculator(BasicCalculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


# Використання класів
basic_calculator = BasicCalculator()
advanced_calculator = AdvancedCalculator()

# Демонстрація роботи базового калькулятора
print("Addition: ", basic_calculator.add(5, 3))
print("Subtraction: ", basic_calculator.subtract(5, 3))

# Демонстрація роботи розширеного калькулятора
print("Addition: ", advanced_calculator.add(5, 3))
print("Subtraction: ", advanced_calculator.subtract(5, 3))
print("Multiplication: ", advanced_calculator.multiply(5, 3))
print("Division: ", advanced_calculator.divide(5, 3))