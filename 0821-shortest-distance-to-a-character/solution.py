class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        
        
        
        
        
        
        length = len(s)
        distances = [0]*len(s)
        
        
        for d in range(length):
            if s[d] != c:
                back = s[0:d]
                front = s[d+1:]
                left = True
                right = True
                try:
                    ld = len(back)- back.rindex(c) 
                except:
                    left = False
                try:
                    rd = front.index(c)+1
                except:
                    right = False
                if left and right:
                    distances[d] = min(ld, rd)
                elif left:
                    distances[d] = ld
                elif right:
                    distances[d] = rd
        
        
        return distances
        
        
        
        
        
        
        """
        prev = float('-inf')
        ans = []
        for i, x in enumerate(s):
            if x == c: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == c: prev = i
            ans[i] = min(ans[i], prev - i)
        
            
        return ans
        """
        
        
        