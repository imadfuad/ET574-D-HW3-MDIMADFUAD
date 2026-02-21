# Write a Python function called calculate_average
# that takes a list of integers as input
# returns the average as a float
# handle empty list by returning 0
# include type hints
from typing import List
def calculate_average(numbers: List[int]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)