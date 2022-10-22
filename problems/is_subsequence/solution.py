class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s[::-1])
        t = list(t[::-1])
        while s:
            if not t:
                return False
            
            if s[-1] == t[-1]:
                s.pop()
            t.pop()
                
        return True
        
        
        