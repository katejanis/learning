import unittest
import subprocess
import square

class SquareTest(unittest.TestCase):

    def test_discriminant(self):
        d = square.disc(1, 2, -1)
        self.assertEqual(d, 8.0)

    def test_solve_mult(self):
        D, r = square.solve(1, -26, 120)
        self.assertEqual(D, 196.0)
        self.assertEqual(r[0], 20.0)
        self.assertEqual(r[1], 6.0)

    def test_solve_single(self):
        D, r = square.solve(-1, 2, -1)
        self.assertEqual(D, 0.0)
        self.assertEqual(r[0], 1.0)

    def test_solve_none(self):
        D, r = square.solve(10, -2, 10)
        self.assertEqual(D, -396.0)
        self.assertEqual(len(r), 0)

    def test_script_mult(self):
        out = subprocess.check_output(['python', 'square.py', '1', '-26', '120'])
        self.assertEqual(out, 'D = 196.0\nx1 = 20.0; x2 = 6.0\n')

    def test_script_single(self):
        out = subprocess.check_output(['python', 'square.py', '-1', '2', '-1'])
        self.assertEqual(out, 'D = 0.0\nx = 1.0\n')

    def test_script_none(self):
        out = subprocess.check_output(['python', 'square.py', '10', '-2', '10'])
        self.assertEqual(out, 'D = -396.0\nNo value\n')


if __name__ == '__main__':
    unittest.main()