import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_float_values(self):
        res = area(5.0, 2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_negative_values_rejected(self):
        with self.assertRaises(ValueError):
            area(-4, 3)

    def test_perimeter_string_type_should_raise(self):
        with self.assertRaises(TypeError):
            perimeter("3", "4", "5")

    def test_perimeter_float_sides(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_invalid_triangle_rejected(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 100)


if __name__ == '__main__':
    unittest.main()