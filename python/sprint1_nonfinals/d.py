from typing import List, Tuple


def get_weather_randomness(temperatures: List[int], n: int) -> int:
    if n == 1:
        return 1
    count = 0
    if temperatures[0] > temperatures[1]:
        count += 1
    if temperatures[n - 1] > temperatures[n - 2]:
        count += 1
    for i in range(1, n - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            count += 1
    return count


def read_input() -> tuple[list[int], int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures, n


temperatures, n = read_input()
print(get_weather_randomness(temperatures, n))
