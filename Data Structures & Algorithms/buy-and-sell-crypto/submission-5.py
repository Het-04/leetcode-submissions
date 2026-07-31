class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        max_profit = 0
        i = 0
        j = 1 
        while j < len(prices): 
            profit = prices[j] - prices[i] 
            if profit > max_profit: 
                max_profit = profit 
                
            elif profit < max_profit and profit < 0:
                i = j
                 
            
            j += 1
        return max_profit

        


            
        
        