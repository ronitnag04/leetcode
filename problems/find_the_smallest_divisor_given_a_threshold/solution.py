class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = sum(nums)//threshold or 1
        r = sum(nums)
        divisor = (l+r)//2
        guess = sum([-(num//-divisor) for num in nums])
        
        while l < r:
            if guess > threshold:
                l = divisor+1
            else:
                r = divisor
            divisor = (l+r)//2
            guess = sum([-(num//-divisor) for num in nums])
        return divisor