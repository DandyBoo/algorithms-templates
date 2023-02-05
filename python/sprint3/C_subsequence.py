def subsequence(substring: str, string: str) -> bool:
    len_sub, len_str = len(substring), len(string)
    if len_sub > len_str:
        return False
    i = 0
    for j in range(len_str):
        if substring[i] == string[j]:
            i += 1
            if i == len_sub:
                return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(subsequence(s, t))
