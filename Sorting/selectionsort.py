# .env
# This file would contain environment variables.
SORT_ALGORITHM=SelectionSort

class SortingStrategy:
    """Interface for sorting strategies."""
    def sort(self, arr):
        raise NotImplementedError("Must implement sort method")

class SelectionSort(SortingStrategy):
    """Implementation of Selection Sort"""
    def sort(self, arr):
        n = len(arr)
        for i in range(0, n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

class SortFactory:
    """Factory for creating sorting algorithm instances."""
    @staticmethod
    def get_sort_strategy(strategy_type):
        if strategy_type == "SelectionSort":
            return SelectionSort()
        # You can add more sorting strategies here if needed.
        raise ValueError(f"Unknown sort strategy: {strategy_type}")

def load_env():
    """Load environment variables for configuration."""
    import os
    return os.getenv("SORT_ALGORITHM")

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    # Load environment variables
    load_dotenv()
    sort_algorithm = load_env()

    sort_factory = SortFactory()
    sorting_strategy = sort_factory.get_sort_strategy(sort_algorithm)

    temp = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in temp.split(",")]
    
    sorted_arr = sorting_strategy.sort(arr)
    print("Sorted array:", sorted_arr)
