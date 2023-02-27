from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    dq = deque()
    l, r = 0, 0

    while r < len(nums):
        while dq and nums[r] > dq[-1]:
            dq.pop()
        dq.append(nums[r])

        if (r - l + 1) == k:
            res.append(dq[0])
            if dq[0] == nums[l]:
                dq.popleft()
            l += 1
        r += 1

    return res


l = [1, 3, -1, -3, 5, 3, 6, 7]
print(maxSlidingWindow(l, 3))
