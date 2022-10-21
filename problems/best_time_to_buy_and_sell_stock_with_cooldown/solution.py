class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1]-prices[0])
        
        possProfits = []
        for i in range(len(prices)-1):
            possProfits.append(prices[i+1]-prices[i])
        possProfits.append(0) 
        
        @lru_cache(None)
        def helper(i, holding):
            if not possProfits[i:]:
                return 0
            else:
                if holding:
                    option1 = helper(i+2, False)
                else:
                    option1 = helper(i+1, False)
                option2 = possProfits[i] + helper(i+1, True)
                return max(option1, option2)
        
        return helper(0, False)
    
    
    """
    [0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 2]
    [0, 0, 0, 0, 0,-3]
    [0, 0, 0, 0, 2, 1]
    [0, 2, 0, 1, 1, 1]
    [0, 2,-3, 1, 1, 0]
    
    """
        