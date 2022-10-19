class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        
        found = dict()
        for num in nums:
            if num in found:
                found[num] += 1
            else:
                found[num] = 1
                
        
        return [num for num in found 
                if found[num] == 1 and num-1 not in found and num+1 not in found]
