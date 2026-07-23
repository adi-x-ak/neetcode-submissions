class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #define an result array and intialize with 1
        result =[1]*len(nums)
        #deine a variable prefix 
        prefix=1
        #loop from left to right first pass 
        for i in range(len(nums)):
            result[i] = prefix
            prefix*=nums[i]
        #now post fix ,from right to left
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]
        return result


        
        