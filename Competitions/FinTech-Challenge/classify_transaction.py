"""
Challenge: Classify Transaction
Platform: CoderHub
Difficulty: Medium
"""

from typing import List

def classifyTransaction(amount: int) -> str:
    if amount < 100:
        return "LOW"
    else:
        return "MEDIUM"


print(classifyTransaction(100))
print(classifyTransaction(98))
