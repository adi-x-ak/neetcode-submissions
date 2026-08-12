class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        profit=0

        for i in range(len(prices)):
            if prices[i]>minprice:
                profit=prices[i]-minprice
                maxprofit=max(maxprofit,profit)
            else:
                minprice=prices[i]
        return maxprofit

        