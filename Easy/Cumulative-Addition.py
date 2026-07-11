from typing import List

def cumulative_addition(elements_array: List[int]) -> List[int]:
    result = []
    total = 0

    for num in elements_array:
        total += num
        result.append(total)

    return result

print(cumulative_addition([1, 2, 3, 4, 5]))
