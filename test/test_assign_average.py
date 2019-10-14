import unittest
from main_program import assign_average as a


class MyTestCase(unittest.TestCase):
    def test_assign_average_using_A(self):
        self.assertEqual(a.switch_average('A'), 90)

    def test_assign_average_using_B(self):
        self.assertEqual(a.switch_average('B'), 80)

    def test_assign_average_using_C(self):
        self.assertEqual(a.switch_average('C'), 70)

    def test_assign_average_using_D(self):
        self.assertEqual(a.switch_average('D'), 60)

    def test_assign_average_using_F(self):
        self.assertEqual(a.switch_average('F'), 0)

    def test_assign_average_using_invalid_key(self):
        self.assertEqual(a.switch_average('Z'), 'Value not found for Z.')


if __name__ == '__main__':
    unittest.main()
