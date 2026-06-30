# from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:

#         n = len(height)
#         if n == 0:
#             return 0

#         res = 0

#         p1 = 0
#         p2 = 1

#         while p2 < n:
#             if height[p2] >= height[p1]:
#                 area = ((p2 - p1 - 1) * min(height[p2], height[p1])) - sum(height[p1 + 1:p2])

#                 if area > 0:
#                     res += area

#                 p1 = p2

#             p2 += 1

#         p1 = n - 1
#         p2 = n - 2

#         while p2 >= 0:
#             if height[p2] > height[p1]:
#                 area = ((p1 - p2 - 1) * min(height[p1], height[p2])) - sum(height[p2 + 1:p1])

#                 if area > 0:
#                     res += area

#                 p1 = p2

#             p2 -= 1

#         return res




from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1

        leftMax = height[l]
        rightMax = height[r]

        res = 0

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                res+= (leftMax-height[l])

            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res+=(rightMax-height[r])

        return res

