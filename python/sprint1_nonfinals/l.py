from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter_list = list(shorter)
    longer_list = list(longer)
    for i in shorter_list:
        longer_list.remove(i)
    return longer_list[0]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
