class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        """ V1 Not Time Efficient
        matches = {}
        
        for num in arr:
            if num not in matches.keys():
                matches[num] = 1
            else:
                matches[num] += 1
        
        arr.sort()
        if 0 in matches.keys():
            if matches[0] % 2 != 0:
                return False
            else:
                del matches[0]
                while 0 in arr:
                    arr.pop(arr.index(0))
        
        while len(arr) > 1:
            temp = arr.pop(0)
            matches[temp] -= 1
            if temp * 2 in matches.keys() and matches[temp*2] > 0:
                nTemp = arr.pop(arr.index(temp*2)) 
                matches[nTemp] -= 1
            elif temp / 2 in matches.keys() and matches[temp/2] > 0:
                
                nTemp = arr.pop(arr.index(temp/2)) 
                matches[nTemp] -= 1
            else:
                return False
        return True
        """
        
        matches = {}
        
        for num in arr:
            if num not in matches.keys():
                matches[num] = 1
            else:
                matches[num] += 1
        
        
        if 0 in matches.keys():
            if matches[0] % 2 != 0:
                return False
            else:
                del matches[0]
        
        while matches:
            temp = min(matches.keys())
            if temp * 2 in matches.keys() and matches[temp*2] > 0:
                if matches[temp] == 1:
                    del matches[temp]
                else:
                    matches[temp] -= 1
                if matches[temp*2] == 1:
                    del matches[temp*2]
                else:
                    matches[temp*2] -= 1
            elif temp / 2 in matches.keys() and matches[temp/2] > 0:
                if matches[temp] == 1:
                    del matches[temp]
                else:
                    matches[temp] -= 1
                if matches[temp/2] == 1:
                    del matches[temp/2]
                else:
                    matches[temp/2] -= 1
            else:
                return False
        return True