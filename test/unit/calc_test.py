import pytest
import unittest
from app.calc import Calculator


@pytest.mark.unit
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-27, self.calc.power(-3, 3))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_zero_division(self):
        with self.assertRaises(TypeError):
            self.calc.divide(1, 0)

    def test_check_types_fails_with_invalid_parameters(self):
        invalid_values = ["2", None, object(), [1, 2], {"key": "value"}]
        for method in [self.calc.add, self.calc.substract, self.calc.multiply, self.calc.divide, self.calc.power]:
            for value in invalid_values:
                # Verifica ambos parámetros con valores inválidos
                with self.assertRaises(TypeError, msg=f"Error en {method.__name__} con {value}"):
                    method(value, 2)
                with self.assertRaises(TypeError, msg=f"Error en {method.__name__} con {value}"):
                    method(2, value)

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_multiply_method_fails_with_invalid_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "0", 0)
        self.assertRaises(TypeError, self.calc.multiply, object(), 0)

    def test_power_method_fails_with_invalid_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "0", 0)
        self.assertRaises(TypeError, self.calc.power, 0, "0")
        self.assertRaises(TypeError, self.calc.power, "0", object())

    def test_substract_method_fails_with_invalid_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "0", 0)
        self.assertRaises(TypeError, self.calc.substract, object(), 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
