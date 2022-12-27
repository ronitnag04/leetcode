class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        temps = s
        
        while len(temps) > k:
            groups = []
            while len(temps) > 0:
                groups.append(temps[0:k])
                temps = temps[k:]
            temps = ''
            for group in groups:
                num = sum([int(num) for num in group])
                temps += str(num)
            print(temps)
        return temps