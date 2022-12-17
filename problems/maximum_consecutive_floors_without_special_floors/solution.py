class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        floors = sorted(special)
        diffs = [floors[i]-floors[i-1]-1 for i in range(1, len(floors))]
        return max(max(diffs if diffs else [-1]), floors[0]-bottom, top-floors[-1])

