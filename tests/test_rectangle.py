import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_typical(self):
        res = area(4.0, 5.0)
        self.assertEqual(res, 20.0)

    def test_area_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_float_sides(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_area_negative_side_rejected(self):
        with self.assertRaises(ValueError):
            area(-4, 5)

    def test_area_string_type_raises(self):
        with self.assertRaises(TypeError):
            area("4", "5")

    def test_area_none_type_raises(self):
        with self.assertRaises(TypeError):
            area(None, 5)

    def test_perimeter_typical(self):
        res = perimeter(4.0, 5.0)
        self.assertEqual(res, 18.0)

    def test_perimeter_string_type_should_raise(self):
        with self.assertRaises(TypeError):
            perimeter("4", "5")

    def test_perimeter_none_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter(None, 5)

    def test_perimeter_zero_sides(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_square_case(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_float_sides(self):
        res = perimeter(2.5, 4.0)
        self.assertAlmostEqual(res, 13.0)


if __name__ == '__main__':
    unittest.main()