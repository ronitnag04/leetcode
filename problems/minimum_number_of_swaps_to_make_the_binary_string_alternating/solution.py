class Solution:
    def minSwaps(self, s: str) -> int:
        
        chars = ['0', '1']
        s0 = 0
        s1 = 0
        counts = {'0':0, '1':0}
        for i, val in enumerate(s):
            counts[val] += 1
            s0 += int(chars[i%2] != val)
            s1 += int(chars[(i+1)%2] != val)
        
        
        if abs(counts['1']-counts['0']) > 1:
            return -1
        
        
        
        if not s0%2 and not s1%2:
            return -(min(s0, s1)//-2)
        elif not s0%2:
            return -(s0//-2)
        else:
            return -(s1//-2)