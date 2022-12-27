class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        signs = [-1 if arr[i]<arr[i-1] else int(arr[i]>arr[i-1]) for i in range(1, len(arr))]
        if -1 not in signs and 1 not in signs:
            return 1
        left = 0
        right = 1
        maxi = 0
        while right <= len(signs):
            if right < len(signs) and signs[right] != 0 and signs[right] == -1*signs[right-1]:
                right += 1
            else:
                maxi = max(maxi, right-left)
                left = right
                right = right+1
        max(maxi, right-left)
        
        return maxi+1
        