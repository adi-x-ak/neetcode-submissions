class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        tmp = {}

        for i in range(len(nums)):
            tmp[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in tmp:
                if tmp.get(target-nums[i]) != i:
                    return [i,tmp.get(target-nums[i])]

        