"""
Challenge: Check Balance
Platform: CoderHub
Difficulty: Easy
"""

from typing import List

def canPay(balance: int, amount: int) -> bool:
    return balance >= amount
print(canPay(785 , 643))