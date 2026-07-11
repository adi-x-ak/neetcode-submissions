class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # mid = len(nums)//2
        # l=0

        # if target<nums[mid]:
        #     for i in range(mid):
        #         if nums[i] == target:
        #             return i
        # else:
        #     for i in range(mid,len(nums)):
        #         if nums[i] == target:
        #             return i

        # return -1

        # l = 0
        # r = len(nums)

        # while l<r:

        #     m = l + ((r-l)//2)

        #     if nums[m] > target:
        #         r = m
        #     elif nums[m] <= target:
        #         l = m + 1
            
        # if l and nums[l-1] == target:
        #     return l-1
        # else:
        #     return -1


        l = 0
        r = len(nums) - 1

        while l<=r:

            m = (r+l)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return -1

                


        