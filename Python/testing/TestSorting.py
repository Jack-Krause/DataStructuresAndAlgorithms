import unittest
from random import randint

from sorting.AlgorithmsSorting import ArraySortingAlgorithm


def sort_checker(actual: list) -> bool:
    return all(actual[i] <= actual[i + 1] for i in range(len(actual) - 1))


class TestSorts(unittest.TestCase):

    def setUp(self):
        self.test_inst = ArraySortingAlgorithm()
        self.simple_input = [1, 0]
        self.simple_solution = [0, 1]
        self.zero_length_input = []
        self.single_length_input = [10]
        self.random_input = [randint(1, 1000) for _ in range(100)]
        self.negative_input = [100, -100, 0, 0, 100, -100]
        self.negative_simple_solution = [-100, -100, 0, 0, 100, 100]
        self.sorted_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.duplicate_input = [1, 1, 1, 1, 1, 1]

    def test_isort_simple(self):
        arr_input = self.simple_input
        arr_input_zero = self.zero_length_input

        arr_actual = self.test_inst.insertion_sort(arr_input)
        arr_actual_zero = self.test_inst.insertion_sort(arr_input_zero)

        self.assertTrue(sort_checker(arr_actual))
        self.assertEqual(self.simple_solution, arr_actual)
        self.assertTrue(sort_checker(arr_actual_zero))

    def test_isort_zero_length(self):
        arr_input = self.zero_length_input
        arr_actual = self.test_inst.insertion_sort(arr_input)

        self.assertTrue(sort_checker(arr_actual))

    def test_isort_random(self):
        arr_input = self.random_input
        arr_actual = self.test_inst.insertion_sort(arr_input)

        self.assertTrue(sort_checker(arr_actual))

    def test_isort_negative_simple(self):
        arr_input = self.negative_input
        arr_actual = self.test_inst.insertion_sort(arr_input)

        self.assertEqual(self.negative_simple_solution, arr_actual)
        self.assertTrue(sort_checker(arr_actual))

    def test_isort_already_sorted(self):
        arr_input = self.sorted_input
        arr_actual = self.test_inst.insertion_sort(arr_input)

        self.assertTrue(sort_checker(arr_actual))

    def test_isort_duplicates(self):
        arr_input = self.duplicate_input
        arr_actual = self.test_inst.insertion_sort(arr_input)

        self.assertTrue(sort_checker(arr_actual))



