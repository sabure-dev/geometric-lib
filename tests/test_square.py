import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_float_side(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_negative_side_rejected(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_string_type_should_raise(self):
        with self.assertRaises(TypeError):
            perimeter("4")

    def test_perimeter_float_side(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)


if __name__ == '__main__':
    unittest.main()