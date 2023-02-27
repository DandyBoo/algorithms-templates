"""
На вход подается строка. Нужно определить длину наибольшей подстроки, которая не содержит повторяющиеся символы.
Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 10 000.
Формат вывода
Выведите натуральное число —– ответ на задачу.
"""


def find_max_substring(s: str) -> int:
    window = ''
    count = 0
    for char in s:
        if char not in window:
            window += char
        else:
            if count < len(window):
                count = len(window)
            window = window[window.index(char) + 1:] + char
    return count if count > len(window) else len(window)


s = input()
print(find_max_substring(s))


# второй способ

def find_max_substring2(s: str) -> int:
    window = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        window.add(s[r])
        res = max(res, r - l + 1)
    return res


print(find_max_substring2(input()))
