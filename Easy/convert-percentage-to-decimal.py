from typing import List

def convertPercent(percentage: str) -> float:
    return float(percentage.replace("%", "")) / 100

print(convertPercent("100"))