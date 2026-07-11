"""
Challenge: Maximum Transaction
Platform: CoderHub
Difficulty: Medium
"""

from typing import List

def maxTransaction(transactions: List[int]) -> int:
    if not transactions:
        return 0

    largest = transactions[0]
    for t in transactions:
        if t > largest:
            largest = t
    return largest


print(maxTransaction([1, 2, 3, 4, 5]))