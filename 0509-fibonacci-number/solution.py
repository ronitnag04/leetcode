class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        def helper(self, n, prev, prev2):
            if n == 1:
                return prev + prev2
            else:
                return helper(self, n-1, prev2+prev, prev)
        
        
        return helper(self, n-1, 1, 0)
        
        
       
        