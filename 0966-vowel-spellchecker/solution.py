class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        def replaceVowels(word):
            return ''.join('_' if c in vowels else c for c in word).lower()
        
        
        caps = {word.lower():word for word in wordlist[::-1]}
        vowelwords = {replaceVowels(word):word for word in wordlist[::-1]}
        wordlist = set(wordlist)
        results = []
        for word in queries:
            result = ''
            if word in wordlist:
                result = word
            elif word.lower() in caps:
                result = caps[word.lower()]
            else:
                stripped = replaceVowels(word)
                if stripped in vowelwords:
                    result = vowelwords[stripped]
                    
            results.append(result)
            
        return results