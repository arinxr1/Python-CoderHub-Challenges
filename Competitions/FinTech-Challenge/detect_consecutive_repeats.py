"""
Challenge: Detect Consecutive Repeats
Platform: CoderHub
Difficulty: Hard
"""

from typing import List

def detectRepeat(transactions: List[int]) -> bool:
    for i in range(len(transactions) - 1):
        if transactions[i] == transactions[i + 1]:
            return True
    return False


print(detectRepeat([100, 100, 200]))
print(detectRepeat([100, 200, 100]))
print(detectRepeat([]))