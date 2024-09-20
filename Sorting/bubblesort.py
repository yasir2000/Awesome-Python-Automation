from abc import ABC, abstractmethod
import os

# .env file content simulation
# BUBBLE_SORT_ARRAY=[2, 1, 10, 23]
def load_env_variables():
    return {
        'BUBBLE_SORT_ARRAY': [int(x) for x in os.getenv('BUBBLE_SORT_ARRAY', '2, 1, 10, 23').split(',')]
    }

# Strategy pattern for sorting algorithms
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, arr):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# Context to use the sorting strategy
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort(self, arr):
        return self.strategy.sort(arr)

# Facade to simplify the API
class SortingFacade:
    def __init__(self):
        self.strategy = BubbleSort()  # This can be replaced with other sorting strategies
        self.sorter = Sorter(self.strategy)

    def perform_sorting(self, arr):
        return self.sorter.sort(arr)

# Main execution
if __name__ == "__main__":
    # Load environment variables
    env_vars = load_env_variables()
    array_to_sort = env_vars['BUBBLE_SORT_ARRAY']

    # Facade usage 
    sorting_facade = SortingFacade()
    sorted_array = sorting_facade.perform_sorting(array_to_sort)

    print("Sorted array is:")
    for i in sorted_array:
        print("%d" % i)
