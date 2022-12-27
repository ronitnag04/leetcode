class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Ds = {}
        for i, c in enumerate(s):
            Ds[c] = Ds.get(c,[]) + [i]
        
        Dt = {}
        for i, c in enumerate(t):
            Dt[c] = Dt.get(c, []) + [i]
            
        Ls = list(Ds.values())
        Lt = list(Dt.values())
        
        while Ls:
            this = Ls.pop()
            try: 
                i = Lt.index(this)
                Lt.pop(i)
            except:
                return False
            
        return True
        
        