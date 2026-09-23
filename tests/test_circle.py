import unittest
import math

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_float_radius(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.634954084936208)

    def test_area_negative_radius_rejected(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_float_radius(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 15.707963267948966)

    def test_perimeter_string_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter("5")


if __name__ == '__main__':
    unittest.main()