class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        largest = 0
        
        def look(r, c):
            if (r,c) in seen:
                return 0
            if not(0 <= r < len(grid)):
                return 0
            if not(0 <= c < len(grid[0])):
                  return 0
            if grid[r][c] == 0:
                   return 0
            seen.add((r,c))
            return 1 + look(r+1, c) + look(r-1, c) + look(r, c+1) + look(r, c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                largest = max(largest, look(r,c))
        
        return largest
                   
            
                   
            
                   
                   
        