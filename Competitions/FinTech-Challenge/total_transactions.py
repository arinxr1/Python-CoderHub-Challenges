"""
Challenge: Total Transactions
Platform: CoderHub
Difficulty: Easy
"""

from typing import List

def totalTransactions(transactions: List[int]) -> int:
    return sum(transactions)

print(totalTransactions([10, 20, 30]))