class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) == 1:
            return s
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        
        found = ""
        
        def findPal(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            
        
        for i in range(len(s)):
            sleft = findPal(self, s, i, i)
            if len(sleft) > len(found):
                found = sleft
            sright = findPal(self, s, i, i+1)
            if len(sright) > len(found):
                found = sright
                
            
        
        return found
        
        
        
    
        