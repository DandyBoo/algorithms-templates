from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    num_int = int(''.join(map(str, number_list)))
    num_sum = num_int + k
    res = [int(i) for i in str(num_sum)]
    return res


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
