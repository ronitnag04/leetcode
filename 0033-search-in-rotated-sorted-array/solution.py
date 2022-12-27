class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] and target > nums[-1]:
            return -1
        
        left = 0
        right = len(nums)-1
        while nums[left] > nums[right] and left+1 < right:
            mid = (right+left)//2
            if nums[mid] > nums[0]:
                left = mid
            if nums[mid] < nums[-1]:
                right = mid
        
        pivot = right
        left = 0
        right = len(nums)-1
        if target >= nums[0]:
            right = pivot
        else:
            left = pivot
            
        while left+1 < right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
            
        return -1
        
        
        
        
        