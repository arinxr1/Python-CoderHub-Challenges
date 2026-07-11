from typing import List
def isPalindrome(s: str) -> bool:
    # write your code here ^_^

    clean = ""

    for c in s:
        if c.isalnum():
            clean += c.lower()

    return clean == clean[::-1]

print(isPalindrome('madam'))