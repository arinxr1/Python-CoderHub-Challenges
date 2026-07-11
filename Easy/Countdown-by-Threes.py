from typing import List

def countdown(num: int) -> List[int]:
    result = []

    for i in range(num - 3, 0, -3):
        if i % 2 == 0:
            result.append(i)

    if len(result) == 0:
        return [0]

    result.sort()
    return result

print(countdown(3))