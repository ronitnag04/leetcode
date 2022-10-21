class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 1 3 5 2 4
        # 4 2 3
        # 7 5 3
        
        life = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if not life:
                    return False
                if i == len(nums)-1: # last element so pass
                    life = False
                elif nums[i-1] == nums[i+1]: # level it out, so pass
                    life = False
                elif nums[i-1] < nums[i+1]: # same value, so pass
                    life = False
                elif nums[i-1] > nums[i+1]:
                    if i-1 == 0:    # first element can be changed, so 
                        life = False
                    elif i-2 >= 0 and nums[i-2] <= nums[i] and nums[i-2] <= nums[i+1]:
                        life = False
                    else:
                        return False
                    
        
        
        return True
    
    
    
