import unittest
from unittest.mock import patch

from io import StringIO

from main import Solution

class TestSolution(unittest.TestCase):

    @patch("sys.stdin", StringIO(open('test.txt', 'r').read()))
    def test_complete(self):
        answer =[(1, 3), (2, 3)] 
        self.assertEqual(answer, Solution().solve())

if __name__ == "__main__":
    unittest.main()
