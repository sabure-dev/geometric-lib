import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_float_sides(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_area_negative_side_rejected(self):
        with self.assertRaises(ValueError):
            area(-4, 5)

    def test_perimeter_float_sides(self):
        res = perimeter(2.5, 4.0)
        self.assertAlmostEqual(res, 13.0)

    def test_perimeter_string_type_should_raise(self):
        with self.assertRaises(TypeError):
            perimeter("4", "5")


if __name__ == '__main__':
    unittest.main()