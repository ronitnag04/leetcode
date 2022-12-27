class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """        
        if not('X' in s):
            return 0
        
        count = 0
        
        while 'X' in s:
            if len(s) <= 3:
                return count + 1
            while s[0] == 'O':
                s = s[1:]
            count += 1          
            s = s[3:]
        
        return count
        
        """
        XXX move
        XXO X move
            O move
        XOX X
            O
        OXX X
            O
        XOO X
            O
        OOX X
            O
        OXO X
            O
        """