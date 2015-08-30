import unittest

from gale_shapley import gale_shapley

from gale_shapley import is_new_partner_better


class TestGale_shapley(unittest.TestCase):
    def test_single_matching(self):
        result = gale_shapley([[1]], [[1]])
        self.assertEqual({(1, 1)}, result)

    def test_partner_better(self):
        self.assertEqual(False, is_new_partner_better([1, 2, 3], 1, 3))
        self.assertEqual(True, is_new_partner_better([1, 2, 3], 3, 2))

    def test_two_pair(self):
        result = gale_shapley([[1, 2], [2, 1]], [[2, 1], [1, 2]])
        self.assertEqual({(1, 1), (2, 2)}, result)

    def test_three_pair(self):
        result = gale_shapley([[1, 2, 3], [2, 1, 3], [1, 2, 3]], [[2, 1, 3], [1, 2, 3], [2, 1, 3]])
        self.assertEqual({(1, 1), (2, 2), (3, 3)}, result)

    def test_three_pair_lying(self):
        result = gale_shapley([[1, 2, 3], [2, 1, 3], [1, 2, 3]], [[2, 1, 3], [1, 3, 2], [2, 1, 3]])
        self.assertEqual({(1, 2), (2, 1), (3, 3)}, result)
