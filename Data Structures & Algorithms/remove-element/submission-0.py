class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:          
      i,j=0,0
      while j<len(nums):
            ele=nums[j]
            if ele!=val:
                  nums[i],nums[j]=nums[j] , nums[i]
                  i+=1
                  j+=1
            
            else:
                  j+=1
            
                
            
      return i



        