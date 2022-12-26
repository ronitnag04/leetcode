class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def helper(s, seen):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                if s in seen:
                    return 0
                else:
                    return 1
            if len(s) == 2:
                if s[0] == s[1]:
                    if s in seen:
                        return 0
                    else:
                        return 1
                else:
                    if s[0] not in seen and s[1] not in seen:
                        return 2
                    else:
                        if s in seen:
                            return 0
                        else:
                            return 1
                       
            routes = []
            for i in range(1, len(s)):
                x = seen.copy()
                if s[:i] not in x:
                    x.add(s[:i])
                    routes.append(1 + helper(s[i:], x))
            
            if routes:
                return max(routes)
            else:
                return 1
        
        t = set()
        return helper(s, t)
            
        
        
        