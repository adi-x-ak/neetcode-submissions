class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = set()
        res2 = []

        for i in range(k):
            res.add(nums[i])

        res2.append(max(nums[0:k]))

        for i in range(1, len(nums) - k +1):

            res2.append(max(nums[i:i+k]))

        return res2



        



            



        
        