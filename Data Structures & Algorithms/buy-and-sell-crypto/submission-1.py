class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        ans = 0
        currLow = prices[0]
        for right in range(len(prices)):
            if prices[right] < currLow:
                currLow = prices[right]
            
            ans = max(ans, prices[right] - currLow)
        
        return ans