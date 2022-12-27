class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left = 0
        right = sum(nums[1:])
        if right == 0:
            return 0
        
        for i in range(1, len(nums)-1):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
            
        if left + nums[-2] == 0:
            return len(nums)-1
        
        return -1
                
        