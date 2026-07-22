class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #lets create a set and that has our nums array
        numset=set(nums)
        #to keep track of longest sequence
        longest=0
        #lets loop through each element in that array and check if nums[i-1] is present
        # if exixits lets keep vhecking for next consecutuive elements 
        for n in nums:
            if (n - 1) not in numset:
                length=0
                while (n + length) in numset:
                    length+=1
                longest=max(longest,length)
        return longest