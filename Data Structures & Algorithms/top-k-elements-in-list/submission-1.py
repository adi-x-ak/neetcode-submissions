import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countN = {}
        for i in range(len(nums)):
            countN[nums[i]] = 1 + countN.get(nums[i],0)

        sorted_dict_desc = dict(sorted(countN.items(), key=operator.itemgetter(1), reverse=True))
        keys_list = list(sorted_dict_desc.keys())
        res = []
        for i in range(k):
            res.append(keys_list[i])
        return res
            
    #    a = {}
    #    b= dict(sorted(a.items(),key = operator.itermgetter(1), reverse=True))     