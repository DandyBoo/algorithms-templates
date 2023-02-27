"""
Дана строка, содержащая буквы //A-Z//:
'AAAABBBCDDEEEFKKRRZZAAVVCC'
Нужно написать функцию RLE, которая выдает строку вида:
'A4B3CD2E3FK2R2Z2A2V2C2'
Еще надо выдавать ошибку если на вход приходит недопустимая строка.

Примечания:
1. Если символ встречается один раз, он остается неизменным
2. Если символ встречается более одного раза,
к нему добавляется число повторений.
"""


def rle(s: str) -> str:
    res = []
    count = 0
    current = ''
    for char in s:
        if not ('A' <= char <= 'Z'):
            raise Exception("Wrong data.")

        if char == current:
            count += 1
        else:
            if count == 1:
                res.append(current)
            elif count > 1:
                res.append(current)
                res.append(str(count))
            current = char
            count = 1
    if count == 1:
        res.append(current)
    elif count > 1:
        res.append(current)
        res.append(str(count))

    return ''.join(res)


print(rle('AAAABBBCDDEEEFKKRRZZAAVVCC'))
assert rle('AAAABBBCDDEEEFKKRRZZAAVVCC') == 'A4B3CD2E3FK2R2Z2A2V2C2'
assert rle('') == ''
assert rle('ABCDEABCDE') == 'ABCDEABCDE'


# второй способ:
def rle(s: str) -> str:
    res = []
    count = 0
    for char in s:
        if not ('A' <= char <= 'Z'):
            raise Exception("Wrong data.")
        if count == 0:
            res.append(char)
            count += 1
            continue
        if char == res[-1]:
            count += 1
            continue
        else:
            if count > 1:
                res.append(str(count))
            count = 1
            res.append(char)
    if count > 1:
        res.append(str(count))

    return ''.join(res)


print(rle('AAAABBBCDDEEEFKKRRZZAAVVCC'))
assert rle('AAAABBBCDDEEEFKKRRZZAAVVCC') == 'A4B3CD2E3FK2R2Z2A2V2C2'
assert rle('') == ''
assert rle('ABCDEABCDE') == 'ABCDEABCDE'
