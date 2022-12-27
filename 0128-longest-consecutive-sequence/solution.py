class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import numpy as np
        
        nums = set(nums)
        
        lstreak = 0
        cstreak = 0
        
        for num in nums:
            if num-1 not in nums:
                cstreak = 1
                cnum = num
                
                while cnum +1 in nums:
                    cstreak +=1
                    cnum +=1
            lstreak = max(lstreak,cstreak)
            
        
        
        return lstreak
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        nums.sort()
        consecs = []
        
        length = 0
        
        
        i = 1
        while len(nums) > 1 and i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            elif nums[i] == 1+nums[i-1]:
                i+=1
            else:
                consecs.append(nums[0:i])
                nums = nums[i:]
                i = 1
        consecs.append(nums)
        
        for i in range(len(consecs)):
            length = max(length, len(consecs[i]))
        
                
        
        return length
        """
        
        
        
        