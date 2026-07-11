from typing import List

def longestAlternatingSubstring(digits: str) -> str:
    if len(digits) == 0:
        return ""

    longest = ""
    current = digits[0]

    for i in range(1, len(digits)):
        if (int(digits[i]) % 2) != (int(digits[i-1]) % 2):
            current += digits[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = digits[i]

    if len(current) > len(longest):
        longest = current

    return longest


print(longestAlternatingSubstring("04"))