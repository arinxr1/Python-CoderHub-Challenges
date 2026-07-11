"""
Challenge: Detect sudden spike
Platform: CoderHub
Difficulty: Hard
"""

from typing import List

def maxSpike(values: List[int]) -> int:
    max_diff = 0

    for i in range(len(values) - 1):
        diff = values[i + 1] - values[i]

        if diff > max_diff:
            max_diff = diff

    return max_diff


print(maxSpike([50, 50, 50 , 80]))