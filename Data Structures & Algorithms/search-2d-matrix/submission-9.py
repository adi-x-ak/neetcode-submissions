class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # arr1 = []

        # for row in matrix:
        #     for item in row:
        #         arr1.append(item)

        # r = len(arr1)
        # l = 0

        # while l < r:
        #     m = l + ((r-l)//2)

        #     if arr1[m] > target:
        #         r = m
        #     elif arr1[m] <= target:
        #         l = m+1
            
        # if l and arr1[l - 1] == target:
        #     return True

        # else:
        #     return False


        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l<=r:
            m = (l + r)//2

            row = m // cols
            col = m % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                l = m +1
            else:
                r = m - 1

        return False 



            




        