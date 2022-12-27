class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        
        td = {}
        for char in t:
            td[char] = 1 + td.get(char, 0)
        
        def checkEnough(d1, d2):
            for key, val in d2.items():
                if not key in d1.keys() or d1[key] < val:
                    return False
            return True
        
        minlength = float('inf')
        minWindow = ""
        
        wd = {}
        l = 0
        r = 0
        
        while r < len(s):
            wd[s[r]] = 1 + wd.get(s[r], 0)
            while l <= r and checkEnough(wd, td):
                if (r+1) - l < minlength:
                    minlength = (r+1) - l
                    minWindow = s[l:r+1]
                
                c = s[l]
                wd[c] -= 1
                l += 1
            r+=1
        return minWindow
            
            
        