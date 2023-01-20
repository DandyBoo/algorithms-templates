from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    num1 = [*map(int, first_number)][::-1]
    num2 = [*map(int, second_number)][::-1]

    # дополнить числа нулями
    size = max(len(num1), len(num2))

    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))

    # сложить 2 числа
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)

    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        res.append(1)

    # перевернуть число назад
    res = res[::-1]

    return ''.join(map(str, res))


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
