import unittest
from unittest.mock import patch

from io import StringIO
import sys

from main import Solution

class TestSolution(unittest.TestCase):

    @patch("sys.stdin", StringIO(open('test.txt', 'r').read()))
    def test_answer(self):
        answer =[(1, 3), (2, 3)] 
        self.assertEqual(answer, Solution().solve())

    @patch("sys.stdin", StringIO(open('test.txt', 'r').read()))
    def test_print(self):
        capturedOutput = StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        Solution().solve()                                # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.

        solFile = open('solution.txt', 'r')
        answer = solFile.read()
        solFile.close()
        # capturedOutput will have the string printed to console with \n
        # characters too
        self.assertEqual(capturedOutput.getvalue(), answer)

if __name__ == "__main__":
    unittest.main()
