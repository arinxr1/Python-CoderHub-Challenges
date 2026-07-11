from typing import List

def sumOdd(arr: List[int]) -> int:
    total = 0

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            total += arr[i]

    return total

print(sumOdd((1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 )))