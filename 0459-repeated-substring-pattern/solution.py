class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:]+s[:-1]
                    
            
        
        
        
        
        """
        for i in range(1, len(s)//2+1):
            if len(s)%i==0:
                sub = s[:i]
                temp = s
                while temp and temp[:i]==sub:
                    temp = temp[i:]
                if not temp:
                    return True
                
        return False
        """
        
        