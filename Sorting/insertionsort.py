# .env
# This file would contain environment variables.

SORT_ALGORITHM=SelectionSort

class SortingStrategy:
    """Interface for different sorting strategies."""
    def sort(self, arr):
        raise NotImplementedError("Must implement sort method")

class InsertionSort(SortingStrategy):
    """Implementation of Insertion Sort"""
    def sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        
        return arr

class SortFactory:
    """Factory for creating sorting algorithm instances"""
    @staticmethod
    def get_sort_strategy(strategy_type):
        if strategy_type == "InsertionSort":
            return InsertionSort()
        # You can add other sorting strategies here (e.g., QuickSort, MergeSort)
        raise ValueError(f"Unknown sort strategy: {strategy_type}")

def load_env():
    """Load environment variables (simulating loading from .env)"""
    import os
    return os.getenv("SORT_ALGORITHM")

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv()
    sort_algorithm = load_env()

    sort_factory = SortFactory()
    sorting_strategy = sort_factory.get_sort_strategy(sort_algorithm)

    arr = [12, 11, 13, 5, 6]
    sorted_arr = sorting_strategy.sort(arr)
    print("Sorted array:", sorted_arr)
