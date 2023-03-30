class Solution:
    def findMin(self, nums: List[int]) -> int:
        f = 0
        l = len(nums)-1
        if (nums[f] < nums[l]):
            return nums[f]
        
        while (nums[f] > nums[l] and f < l-1):
            m = (f+l)//2
            if (nums[m] > nums[f]):
                f = m
            else:
                l = m
        
        return nums[l]
