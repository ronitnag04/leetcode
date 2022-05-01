class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sparse = ""
        for letter in range(len(s)):
            if s[letter] != "#":
                sparse += s[letter]
            else:
                sparse = sparse[:-1]
        
        tparse = ""
        for letter in range(len(t)):
            if t[letter] != "#":
                tparse += t[letter]
            else:
                tparse = tparse[:-1]
        
        return sparse == tparse