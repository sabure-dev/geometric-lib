import unittest
import math

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_typical(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_area_zero_radius(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit_radius(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_float_radius(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.634954084936208)

    def test_area_negative_radius_rejected(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_string_type_raises(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_area_none_type_raises(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_typical(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_radius(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_float_radius(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 15.707963267948966)

    def test_perimeter_string_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_perimeter_none_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()