class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        largest = 0
        increasing = False
        decreasing = False
        i = 0
        cur = 0
        while i < len(arr)-1:
            if not increasing and not decreasing:
                increasing = arr[i] < arr[i+1]
                decreasing = arr[i] > arr[i+1]
                if increasing:
                    cur += 2
            elif increasing:
                if arr[i] < arr[i+1]:
                    cur += 1
                elif arr[i] > arr[i+1]:
                    cur += 1
                    increasing = False
                    decreasing = True
                else:
                    increasing = False
                    cur = 0
            elif decreasing:
                if cur:
                    if arr[i] > arr[i+1]:
                        cur += 1
                    elif arr[i] <= arr[i+1]:
                        largest = max(cur, largest)
                        cur = 0
                        decreasing = False
                        if arr[i] < arr[i+1]:
                            cur = 2
                            increasing = True
                else:
                    if arr[i] < arr[i+1]:
                        decreasing = False
                        increasing = True
                        cur += 2
            i += 1
        if decreasing:
            largest = max(largest, cur)
        
        return largest
        