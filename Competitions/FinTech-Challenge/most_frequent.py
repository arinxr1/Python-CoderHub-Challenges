"""
Challenge: Most Frequent
Platform: CoderHub
Difficulty: Hard
"""
from typing import List

def isSuspiciousPattern(transactions: List[int]) -> bool:
    if not transactions:
        return False

    first = transactions[0]
    for t in transactions:
        if t != first:
            return False

    return True


print(isSuspiciousPattern([50, 50, 50]))
print(isSuspiciousPattern([50, 60, 50]))