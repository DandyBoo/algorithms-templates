import re


def is_palindrome(line: str) -> bool:
    # l1 = re.sub(r'\W+', '', line)
    # l2 = l1.lower()
    # return l2 == l2[::-1]
    l_p = 0
    r_p = len(line) - 1

    while l_p < r_p:
        l_c = line[l_p]
        if not ('A' <= l_c <= 'Z' or 'a' <= l_c <= 'z' or '0' <= l_c <= '0'):
            l_p += 1
            continue
        r_c = line[r_p]
        if not ('A' <= r_c <= 'Z' or 'a' <= r_c <= 'z' or '0' <= r_c <= '0'):
            r_p -= 1
            continue
        if l_c.upper() != r_c.upper():
            return False
        l_p += 1
        r_p -= 1
    return True


print(is_palindrome(input().strip()))
