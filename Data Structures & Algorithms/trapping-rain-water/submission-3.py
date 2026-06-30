from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n == 0:
            return 0

        res = 0

        # Left to right
        p1 = 0
        p2 = 1

        while p2 < n:
            if height[p2] >= height[p1]:
                area = ((p2 - p1 - 1) * min(height[p2], height[p1])) - sum(height[p1 + 1:p2])

                if area > 0:
                    res += area

                p1 = p2

            p2 += 1

        # Right to left
        p1 = n - 1
        p2 = n - 2

        while p2 >= 0:
            if height[p2] > height[p1]:
                area = ((p1 - p2 - 1) * min(height[p1], height[p2])) - sum(height[p2 + 1:p1])

                if area > 0:
                    res += area

                p1 = p2

            p2 -= 1

        return res