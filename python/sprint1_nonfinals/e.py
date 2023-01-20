def get_longest_word(line: str) -> str:
    list_line = line.split()
    longest = list_line[0]
    for word in list_line:
        if len(word) > len(longest):
            longest = word
    return longest


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
