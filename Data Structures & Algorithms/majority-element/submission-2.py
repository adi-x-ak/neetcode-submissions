class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=0
        count=0
        for i in range(len(nums)):
            if count==0:
                result=nums[i]
                count+=1
            elif nums[i] == result:
                count+=1
            else:
                count-=1
        return result