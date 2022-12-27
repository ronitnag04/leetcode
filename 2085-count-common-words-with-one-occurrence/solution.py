class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        
        words = set()
        
        for word in words1:
            if word not in words:
                if words1.count(word) == 1 and words2.count(word) == 1:
                    words.add(word)
        for word in words2:
            if word not in words:
                if words1.count(word) == 1 and words2.count(word) == 1:
                    words.add(word)
                
        
        return len(words)
        
        """
        c1 = Counter(words1)
        c2 = Counter(words2)
        count = 0
        for word in c1.keys():
            if c1[word] == 1 and c2[word] == 1:
                count +=1
        return count
        """