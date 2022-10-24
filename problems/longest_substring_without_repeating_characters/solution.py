class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        long = 0
        left = 0
        right = 0
        ins = set(s[0])
        while right < len(s):
            while s[right] in ins and left < right:
                ins.remove(s[left])
                left += 1
            
            long = max(long, right-left+1)
            ins.add(s[right])
            right += 1
        
        return long
        
        
        """ O(n^2)
        long = 0
        for i in range(len(s)-1):
            left = i
            right = i+1
            while right < len(s):
                if s[right] not in s[left:right]:
                    right += 1
                else:
                    long = max(long, right-left)
                    left = right
                    right = left+1
            long = max(long, right-left)
        return long
        """