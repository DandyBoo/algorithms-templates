input_string = input()


def br_seq(s: str) -> bool:
    stack = []
    for ch in s:
        if ch not in ['(', ')', '[', ']', '{', '}']:
            return False
        if ch in ['(', '[', '{']:
            stack.append(ch)
        if ch in [')', ']', '}']:
            if len(stack) == 0:
                return False
            open_bracket = stack.pop()
            if open_bracket == '(' and ch == ')':
                continue
            if open_bracket == '[' and ch == ']':
                continue
            if open_bracket == '{' and ch == '}':
                continue
            return False
    if len(stack) == 0:
        return True
    return False


if __name__ == '__main__':
    print(br_seq(input_string))
