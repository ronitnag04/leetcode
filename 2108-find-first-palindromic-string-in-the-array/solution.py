class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if len(word) == 1:
                return word
            if word[::-1] == word:
                return word
        
        return ""
        