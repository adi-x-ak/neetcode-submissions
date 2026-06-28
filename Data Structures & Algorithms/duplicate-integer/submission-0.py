class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''algorithm   
        1) we will iterate through the list
        we need to check if the element s already in hashset or not 
        2) put each element in hashset 
        3) since hashset doesnt allow duplicate the value '''
        duplicate = set()
        for i in range(len(nums)):
            element = nums[i]
            if element in duplicate:
                return True
            else:
                duplicate.add(element)
        return False

            
    
        
     
        