class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr1 = []

        for row in matrix:
            for item in row:
                arr1.append(item)

        r = len(arr1)
        l = 0

        while l < r:
            m = l + ((r-l)//2)

            if arr1[m] > target:
                r = m
            elif arr1[m] <= target:
                l = m+1
            
        if l and arr1[l - 1] == target:
            return True

        else:
            return False
        