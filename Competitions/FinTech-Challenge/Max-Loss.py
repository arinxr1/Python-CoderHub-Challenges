"""
Challenge: Max Loss
Platform: CoderHub
Difficulty: Hard
"""

from typing import List

def maxLoss(values: List[int]) -> int:
    if len(values) == 0:
        return 0

    highest = values[0]
    loss = 0

    for i in range(len(values)):
        if values[i] > highest:
            highest = values[i]

        if highest - values[i] > loss:
            loss = highest - values[i]

    return loss

print(maxLoss([50, 50, 50]))
