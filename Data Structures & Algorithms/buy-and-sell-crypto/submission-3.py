class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #intialize l at starting and r at index i which is next to l
        l,r=0,1
        # if prices at l is less that at r it means we can make some profit so caculate
        #if not move left to thr right pointer and move r pointer to one place an update 
        maxprofit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxprofit=max(maxprofit,profit)
            else:
                l=r
            r+=1
        return maxprofit 

        