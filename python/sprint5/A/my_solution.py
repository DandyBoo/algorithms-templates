# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    if root is None:
        return -1

    result = root.value
    left_result = solution(root.left)
    right_result = solution(root.right)
    if left_result > result:
        result = left_result
    if right_result > result:
        result = right_result
    return result


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
