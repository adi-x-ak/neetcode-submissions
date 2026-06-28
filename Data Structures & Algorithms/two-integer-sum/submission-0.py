class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}   #craete a map 
        for i in range(len(nums)):
            curr=nums[i]
            diff=target-curr
            if diff in indices:
                return [indices[diff],i]
            indices[curr]=i
         








# {3:0,4:1,5:2,6:3}

#{3:0 ,}



        