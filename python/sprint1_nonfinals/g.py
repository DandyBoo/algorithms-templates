def to_binary(number: int) -> int:
    if number < 2:
        return number
    res = []
    while True:
        res.append(number % 2)
        number = number // 2
        if number < 2:
            res.append(number)
            break
    res.reverse()
    for i in range(len(res)):
        s = ''.join(str(i) for i in res)
    return int(s)


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
