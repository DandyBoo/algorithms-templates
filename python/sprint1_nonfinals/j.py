from typing import List


def factorize(number: int) -> List[int]:
    i = 2
    res = []
    while i * i <= number:
        while number % i == 0:
            res.append(i)
            number /= i
        i += 1
    if number > 1:
        res.append(int(number))
    return res


result = factorize(int(input()))
print(" ".join(map(str, result)))
