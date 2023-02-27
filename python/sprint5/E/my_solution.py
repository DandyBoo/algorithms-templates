# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from math import inf

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    def helper(node, min, max):
        if not node:
            return True
        if not min < node.value < max:
            return False
        return helper(node.left, min, node.value) and helper(node.right, node.value, max)

    return helper(root, -inf, inf)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
