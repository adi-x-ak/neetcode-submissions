class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build a hashmap to store frequencies
        count={}

        #lets create an array where the freqiencies denote the indices and we store the number accoring to the frequency 
        freq=[[] for i in range(len(nums)+1)]

        #lets build the hashmap
        for n in nums:
            count[n]=1+count.get(n,0)
        #build frequency
        for n,c in count.items():
            freq[c].append(n)

        #lets builld result array 
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if(len(res)==k):
                    return res