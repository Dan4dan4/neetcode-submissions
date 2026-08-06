class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if i < j:
                    if prices[j]- prices[i] > best:
                        best = prices[j]- prices[i]
        return best