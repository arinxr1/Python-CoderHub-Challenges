"""
Challenge: Maximum Loss
Platform: CoderHub
Difficulty: Hard
"""

from typing import List

def maxLoss(values: List[int]) -> int:
    if not values:
        return 0

    max_value = values[0]
    max_loss = 0

    for value in values:
        if value > max_value:
            max_value = value
        else:
            loss = max_value - value
            if loss > max_loss:
                max_loss = loss

    return max_loss

print(maxLoss([100, 80, 60, 90]))