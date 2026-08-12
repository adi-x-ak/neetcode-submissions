class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #use hashmap to store number and index when we see aduplicate check the     condition and return 

        maplookup={}
        for i in range(len(nums)):
            if nums[i] in maplookup and i-maplookup[nums[i]]<=k:
                return True
            maplookup[nums[i]]=i
        return False
                


        