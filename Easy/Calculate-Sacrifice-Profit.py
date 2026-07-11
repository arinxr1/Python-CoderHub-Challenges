from typing import List

def calculateSacrificeProfit(buyPrices: List[float], sellPrices: List[float]) -> float:
    profit = 0

    for i in range(len(buyPrices)):
        profit += sellPrices[i] - buyPrices[i]

    return profit

print(calculateSacrificeProfit([4.5, 3, 6], [6, 5, 8]))