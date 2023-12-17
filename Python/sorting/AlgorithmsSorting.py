

class ArraySortingAlgorithm:

    @staticmethod
    def insertion_sort(arr: list) -> list:
        n = len(arr)
        if n <= 1:
            return arr

        for i in range(1, n):
            key_val = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key_val:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key_val

        return arr

