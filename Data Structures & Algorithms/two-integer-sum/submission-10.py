class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #algorithm 
        '''1)reate a hashmap 
        2)iterate through each elem in array add in hashmap along with index )
        at each step u should cal target - key check if that exists in hashmap
        if so return key of the current and existing 
        else put in hashmap 


        0(n)


        '''


        num_idx_map = {}

        for i in range(len(nums)):
            val= target - nums[i]
            if val in num_idx_map:
                return [num_idx_map[val] , i]
            else:
                num_idx_map[nums[i]]=i

                

            

        