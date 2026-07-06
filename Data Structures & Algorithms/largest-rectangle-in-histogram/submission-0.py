class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        n = len(heights)

        for i in range(n+1):

            curr_height = heights[i] if i<n else 0

            while stack and curr_height < heights[stack[-1]]:

                height = heights[stack.pop()]

                right = i-1


                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0

                width = right - left +1
                area = height * width

                max_area = max(max_area,area)

            stack.append(i)

        return max_area


        