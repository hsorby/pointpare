import os
import unittest

from pointpare import PointPare

file_path = os.path.dirname(os.path.realpath(__file__))

TEST_POINTS = [[-10.4498, 31.1871, 1161.39], [-9.26793, 26.6263, 1162.51], [-8.96271, 27.5622, 1161.49], [-10.4498, 31.1871, 1161.39], [-10.7776, 29.8503, 1162.7], [-9.26793, 26.6263, 1162.51], [-10.7776, 29.8503, 1162.7], [-9.7928, 25.6393, 1163.65], [-9.26793, 26.6263, 1162.51], [-10.7776, 29.8503, 1162.7], [-11.2968, 28.4809, 1164.04], [-9.7928, 25.6393, 1163.65], [-11.2968, 28.4809, 1164.04], [-10.4743, 24.635, 1164.8], [-9.7928, 25.6393, 1163.65], [-11.2968, 28.4809, 1164.04], [-11.9597, 27.1357, 1165.3], [-10.4743, 24.635, 1164.8], [-11.9597, 27.1357, 1165.3], [-11.2493, 23.6471, 1165.85], [-10.4743, 24.635, 1164.8], [-11.9597, 27.1357, 1165.3], [-12.7182, 25.8716, 1166.4], [-11.2493, 23.6471, 1165.85], [-12.7182, 25.8716, 1166.4], [-12.0549, 22.7096, 1166.7], [-11.2493, 23.6471, 1165.85], [-12.7182, 25.8716, 1166.4], [-13.5244, 24.7453, 1167.24], [-12.0549, 22.7096, 1166.7], [-13.5244, 24.7453, 1167.24], [-12.828, 21.8561, 1167.25], [-12.0549, 22.7096, 1166.7]]
TEST_POINTS_FLAT_LIST = [-10.4498, 31.1871, 1161.39, -9.26793, 26.6263, 1162.51, -8.96271, 27.5622, 1161.49, -10.4498, 31.1871, 1161.39, -10.7776, 29.8503, 1162.7, -9.26793, 26.6263, 1162.51, -10.7776, 29.8503, 1162.7, -9.7928, 25.6393, 1163.65, -9.26793, 26.6263, 1162.51, -10.7776, 29.8503, 1162.7, -11.2968, 28.4809, 1164.04, -9.7928, 25.6393, 1163.65, -11.2968, 28.4809, 1164.04, -10.4743, 24.635, 1164.8, -9.7928, 25.6393, 1163.65, -11.2968, 28.4809, 1164.04, -11.9597, 27.1357, 1165.3, -10.4743, 24.635, 1164.8, -11.9597, 27.1357, 1165.3, -11.2493, 23.6471, 1165.85, -10.4743, 24.635, 1164.8, -11.9597, 27.1357, 1165.3, -12.7182, 25.8716, 1166.4, -11.2493, 23.6471, 1165.85, -12.7182, 25.8716, 1166.4, -12.0549, 22.7096, 1166.7, -11.2493, 23.6471, 1165.85, -12.7182, 25.8716, 1166.4, -13.5244, 24.7453, 1167.24, -12.0549, 22.7096, 1166.7, -13.5244, 24.7453, 1167.24, -12.828, 21.8561, 1167.25, -12.0549, 22.7096, 1166.7]


class PointPareTestCase(unittest.TestCase):

    def test_creation(self):
        pp = PointPare()
        self.assertEqual(0, len(pp.get_pared_points()))

    def test_add_point(self):
        pp = PointPare()

        pp.add_point(TEST_POINTS[0])

        self.assertEqual(1, len(pp.get_points()))

    def test_add_points(self):
        pp = PointPare()

        pp.add_points(TEST_POINTS)

        self.assertEqual(33, len(pp.get_points()))

    def test_add_flat_points(self):
        pp = PointPare()

        pp.add_points(TEST_POINTS_FLAT_LIST)

        self.assertEqual(33, len(pp.get_points()))

    def test_pare_points(self):
        pp = PointPare()

        pp.add_points(TEST_POINTS)
        pp.pare_points()

        self.assertEqual(33, len(pp.get_points()))
        self.assertEqual(13, len(pp.get_pared_points()))

    def test_get_pared_index(self):
        pp = PointPare()

        pp.add_points(TEST_POINTS)
        pp.pare_points()

        self.assertEqual(33, len(pp.get_points()))
        self.assertEqual(13, len(pp.get_pared_points()))

        self.assertEqual(3, pp.get_pared_index(9))
        self.assertEqual(7, pp.get_pared_index(18))
        self.assertEqual(9, pp.get_pared_index(27))

    def test_clear_points(self):
        pp = PointPare()

        pp.add_points(TEST_POINTS)
        pp.pare_points()

        self.assertEqual(33, len(pp.get_points()))
        self.assertEqual(13, len(pp.get_pared_points()))

        pp.clear_points()

        self.assertEqual(0, len(pp.get_points()))
        self.assertEqual(0, len(pp.get_pared_points()))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
