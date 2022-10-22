class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def replace(n):
            if n in seen:
                return False
            seen.add(n)
            
            if n == 1:
                return True
            
            count = 0
            while n:
                count += (n%10) ** 2
                n //= 10
            return replace(count)
        
        return replace(n)
            
        