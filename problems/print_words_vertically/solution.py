class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        layers = []
        for i in range(len(max(words, key=len))):
            layer = ''
            maxi = -1
            for j, word in enumerate(words):
                if i < len(word):
                    layer += word[i]
                    maxi = j
                else:
                    layer += " "
            layers.append(layer[:maxi+1]) 
        return layers