# 66. Plus One (easy)
def plus_one(digits: list[int]) -> list[int]:
    str_digit = ''.join([str(digit) for digit in digits])
    digits = list(map(int, str(int(str_digit) + 1)))

    return digits


# 202. Happy Number (easy)
def is_happy(n: int) -> bool:
    s: set[int] = set()

    while n != 1:
        if n in s:
            return False
        n = sum([int(digit)**2 for digit in str(n)])
    return True