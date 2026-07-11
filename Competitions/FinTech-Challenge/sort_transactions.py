"""
Challenge: Sort Transactions
Platform: CoderHub
Difficulty: Hard
"""

from typing import List

def sortTransactions(transactions: List[int]) -> List[int]:
    return sorted(transactions)

print(sortTransactions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sortTransactions([300, 100, 200]))