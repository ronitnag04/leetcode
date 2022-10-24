class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2 != 0:
            return False
        half = s//2
        
        
        sums = set()
        for num in nums:
            new = set()
            for s in sums:
                if num+s <= half:
                    new.add(num+s)
            sums = sums.union(new)
            sums.add(num)
            if half in sums:
                return True
            
        print(sums)
        return half in sums
                
        
        
        