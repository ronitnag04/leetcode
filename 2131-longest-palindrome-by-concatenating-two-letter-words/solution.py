class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        d = {}
        for word in words:
            if word in d.keys():
                d[word] += 2
            else:
                d[word] = 2
                
        
        count = 0
        middle = True
        for word, val in d.items():
            if word[0] == word[1]:
                if val%4 == 0:
                    count += d[word]
                    d[word] = 0
                else:
                    used = d[word]//4 * 4
                    if middle:
                        used += 2
                        middle = False
                    count += used
                    d[word] -= used
            else:
                o = d.get(word, 0)
                r =  d.get(word[::-1], 0)
                if o and r:
                    used = min(o, r)
                    d[word] -= used
                    d[word[::-1]] -= used
                    count += used*2
                    
                
                
        
        return count