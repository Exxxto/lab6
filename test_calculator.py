"""
Unit-тесты для калькулятора
"""
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Тестовый класс для проверки функциональности калькулятора"""

    def setUp(self):
        """Инициализация калькулятора перед каждым тестом"""
        self.calc = Calculator()

    def test_add(self):
        """Тест сложения"""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_divide(self):
        """Тест деления"""
        self.assertEqual(self.calc.divide(20, 4), 5)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_factorial(self):
        """Тест вычисления факториала"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)

    def test_factorial_negative(self):
        """Тест факториала отрицательного числа"""
        with self.assertRaises(ValueError):
            self.calc.factorial(-5)


if __name__ == "__main__":
    unittest.main()
