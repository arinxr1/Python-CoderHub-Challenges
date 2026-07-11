"""
Challenge: Unique Transactions
Platform: CoderHub
Difficulty: Medium
"""

from typing import List

def uniqueTransactions(transactions: List[int]) -> List[int]:
    result = []
    for t in transactions:
        if t not in result:
            result.append(t)
    return result


print(uniqueTransactions([10, 20, 10, 30]))