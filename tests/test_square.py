import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_typical(self):
        res = area(4.0)
        self.assertEqual(res, 16.0)

    def test_area_zero_side(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit_side(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_float_side(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_negative_side_rejected(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_area_string_type_raises(self):
        with self.assertRaises(TypeError):
            area("4")

    def test_area_none_type_raises(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_perimeter_typical(self):
        res = perimeter(4.0)
        self.assertEqual(res, 16.0)

    def test_perimeter_string_type_should_raise(self):
        with self.assertRaises(TypeError):
            perimeter("4")

    def test_perimeter_none_type_raises(self):
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_perimeter_zero_side(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit_side(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_float_side(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)


if __name__ == '__main__':
    unittest.main()