from unittest import TestCase

from heap import Heap


class TestHeap(TestCase):
    def test_create_heap(self):
        heap = Heap()

        heap.insert(1)

        self.assertEqual([1], heap.representation())

    def test_swap(self):
        heap = Heap()
        heap.insert(2)
        heap.insert(1)

        heap.swap(1, 2)

        self.assertEqual([1, 2], heap.representation())

    def test_insert(self):
        heap = Heap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)

        self.assertEqual([3, 1, 2], heap.representation())

    def test_find_max_with_empty_heap(self):
        heap = Heap()
        with self.assertRaises(Exception):
            heap.find_max()

    def test_find_max(self):
        heap = Heap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(5)
        heap.insert(3)
        heap.insert(4)

        self.assertEqual(5, heap.find_max())

    def test_delete_left_bigger(self):
        heap = Heap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(5)
        heap.insert(3)
        heap.insert(4)

        heap.delete(1)

        self.assertEqual([4, 3, 2, 1], heap.representation())

    def test_delete_right_bigger(self):
        heap = Heap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(4)
        heap.insert(1)
        heap.insert(2)

        heap.delete(1)

        self.assertEqual([4, 3, 2, 1], heap.representation())
