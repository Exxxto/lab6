class Calculator:
    """Класс калькулятора с базовыми операциями"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def factorial(self, n):
        """Вычисление факториала числа"""
        if n < 0:
            raise ValueError("Факториал отрицательного числа не определен")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    """Главная функция для демонстрации работы калькулятора"""
    calc = Calculator()
    
    print("=== Демонстрация калькулятора ===")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 4 = {calc.divide(20, 4)}")
    print(f"5! = {calc.factorial(5)}")


if __name__ == "__main__":
    main()
