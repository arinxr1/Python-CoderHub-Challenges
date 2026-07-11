from typing import List

def calculateTotalFastingTime(startTimes: List[str], endTimes: List[str]) -> float:
    total = 0.0

    for i in range(len(startTimes)):
        start_h, start_m = map(int, startTimes[i].split(":"))
        end_h, end_m = map(int, endTimes[i].split(":"))

        start = start_h + start_m / 60
        end = end_h + end_m / 60

        total += end - start

    return total


print(calculateTotalFastingTime(["04:30", "06:43"], ["17:34", "18:43"]))
