class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        numCount = Counter(nums)
        
        for i, num in enumerate(nums):
            if numCount[num] > 1:
                dis = 1
                while dis <= k:
                    if i-dis >= 0 and nums[i-dis] == num:
                        return True
                    if i+dis < len(nums) and nums[i+dis] == num:
                        return True
                    dis +=1
        
        
        
        return False
        