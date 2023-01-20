# 80518935
def typing(k, matrix):
    deleted = set()
    score = {}
    max_keys = k * 2
    for i in matrix:
        if i != '.' and i not in deleted:
            score[i] = score.get(i, 0) + 1
            if score[i] > max_keys:
                deleted.add(i)
                del score[i]
    return len(score)


def read_input():
    k = int(input())
    matrix_list = [input() for i in range(4)]
    matrix = ''.join(matrix_list)
    return k, matrix


if __name__ == '__main__':
    k, matrix = read_input()
    print(typing(k, matrix))
