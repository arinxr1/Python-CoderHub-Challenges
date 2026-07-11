"""
Challenge: Fraud Detection
Platform: CoderHub
Difficulty: Medium
"""

from typing import List

def countFraud(transactions: List[int], limit: int) -> int:
    return sum(t > limit for t in transactions)


print(countFraud([100, 1000, 50], 500))