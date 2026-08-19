class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        result=float("inf") # to keep track of the smallest e have found so for 
        total=0

        #i will start looping the the array 
        for right in range(len(nums)):
            total+=nums[right]

            while total>=target:
                result=min(result,right-left+1)
                total-=nums[left]
                left+=1
        if result==float("inf"):
            return 0
        
        return result
            

        