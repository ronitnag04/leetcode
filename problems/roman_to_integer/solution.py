class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key = {
              'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
        
        place = {
              'I':1,
              'V':2,
              'X':3,
              'L':4,
              'C':5,
              'D':6,
              'M':7}
        
        
        total = 0
        if len(s) == 1:
            return key[s]
        for i in range(len(s)-1):
            if place[s[i]] >= place[s[i+1]]:
                total += key[s[i]]
            else:
                total -= key[s[i]]
        total += key[s[-1]]
        
        return total
        