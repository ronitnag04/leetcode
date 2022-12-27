class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        last = 0
        ks = []
        maxi = (1 << maximumBit)-1
        
        
        for val in nums:
            new = last ^ val            
            ks.append(maxi ^ new)
            last = new
        return ks[::-1]
        """
        1 1 1 1 1
        0 1 0 0 1   1 0 1 1 0
        """
        
        
        