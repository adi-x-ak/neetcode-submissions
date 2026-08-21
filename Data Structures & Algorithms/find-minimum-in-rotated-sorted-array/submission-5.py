class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        answer=float("inf")
        

        while low<=high:
            mid=high+low//2

            if nums[low]<=nums[mid]:
                answer=min(answer,nums[low])
                low=mid+1
            else:
                answer=min(answer,nums[mid])
                high=mid-1
        
        return answer


        