def allSameCase(word: str) -> bool:
    return word.islower() or word.isupper()

print(allSameCase("hello"))