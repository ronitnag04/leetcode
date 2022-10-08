class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        know = {}
        for key, value in knowledge:
            know[key] = value
        i = 0
        key = ''
        rs = ''
        while i < len(s):
            if key:
                if s[i] == ')':
                    rs += know.get(key[1:], '?')
                    key = ''
                else:
                    key += s[i]
            else:
                if s[i] == '(':
                    key = '('
                else:
                    rs += s[i]
            i+=1
        return rs
        
        