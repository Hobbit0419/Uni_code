# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        print('\nTests count')
        self.assertEqual(count(4, []), 0)
        self.assertEqual(count([], []), 0)
        self.assertEqual(count(4, [4, 1, 2, 3, 4, 5, 2, 3, 4]), 3)
        self.assertEqual(count([1,2], [4, [1,2,3], [1,2], 3, 'hello']), 1)
        self.assertEqual(count(4, [1, 4, 2, ['a', [[4], 3, 4]]]), 3)
        self.assertEqual(count(True, [72, 78.25, 'iWCEr', False, [5, 33.5, 'AsARE', False, [98, 48.07, 'kxSRX', False, [85, 80.12, 'gSbrX', True]]]]), 1)
        self.assertEqual(count(5, [1, 4, 2, ['a', [[4], 3, 4]]]), 0)
        print('\nTests passed checking list integrity')
        testlist = [4, [1,2,3], [1,2], 3, 'hello']
        listcopy = [4, [1,2,3], [1,2], 3, 'hello']
        count(4, testlist)
        self.assertEqual(testlist, listcopy)
if __name__ == "__main__":
    unittest.main()
