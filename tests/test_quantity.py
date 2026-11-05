import unittest

from warehouse.quantity import parse_quantity


class QuantityParserTests(unittest.TestCase):
    def test_valid_integer(self):
        self.assertEqual(parse_quantity("10"), 10)

    def test_strips_whitespace(self):
        self.assertEqual(parse_quantity("  5  "), 5)

    def test_zero_is_allowed(self):
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")

    def test_non_integer_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("abc")
