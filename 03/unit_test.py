#!/usr/bin/env python3

import unittest
import find_in_partially_sorted_array


class FindInPartiallySortedArrayTest(unittest.TestCase):

    def test_exist_1(self):
        self.assertTrue(
            find_in_partially_sorted_array.find(1, [[1, 2, 3],
                                                    [3, 4, 5],
                                                    [5, 6, 7]]))

    def test_exist_2(self):
        self.assertTrue(
            find_in_partially_sorted_array.find(5, [[1, 2, 3],
                                                    [2, 3, 4],
                                                    [5, 6, 7]]))

    def test_exist_3(self):
        self.assertTrue(
            find_in_partially_sorted_array.find(6, [[1, 2, 3],
                                                    [3, 4, 5],
                                                    [5, 6, 7]]))

    def test_not_exist_1(self):
        self.assertFalse(
            find_in_partially_sorted_array.find(6, []))

    def test_not_exist_2(self):
        self.assertFalse(
            find_in_partially_sorted_array.find(4, [[1, 2, 3, 6],
                                                    [2, 3, 5, 8],
                                                    [3, 6, 7, 9]]))

    def test_not_exist_3(self):
        self.assertFalse(
            find_in_partially_sorted_array.find(0, [[1, 2, 3, 6],
                                                    [2, 3, 5, 8],
                                                    [3, 6, 7, 9]]))

    def test_not_exist_4(self):
        self.assertFalse(
            find_in_partially_sorted_array.find(10, [[1, 2, 3, 6],
                                                     [2, 3, 5, 8],
                                                     [3, 6, 7, 9]]))


if __name__ == '__main__':
    unittest.main()
