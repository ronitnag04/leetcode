class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        oranges = 0
        rots = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    oranges += 1
                elif grid[row][col] == 2:
                    rots.append((row, col))
                    
        time = 0
        while oranges and rots:
            time += 1
            for _ in range(len(rots)):
                rowr, colr = rots.popleft()
                nexts = ((rowr-1, colr), (rowr+1,colr), (rowr, colr-1), (rowr, colr+1))
                for r, c in nexts:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        if grid[r][c] == 1:
                            oranges -= 1
                            grid[r][c] = 2
                            rots.append((r,c))
            
            
            
        if oranges:
            return -1
        return time
        
        
        """
        oranges = set()
        rots = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    oranges.add((row, col))
                elif grid[row][col] == 2:
                    rots.add((row, col))
        
        maxtime = len(grid) * len(grid[0])
        time = 0
        while oranges and time < maxtime:
            changes = set()
            for rowr, colr in rots:
                nexts = ((rowr-1, colr), (rowr+1,colr), (rowr, colr-1), (rowr, colr+1))
                for n in nexts:
                    if n in oranges:
                        oranges.remove(n)
                        changes.add(n)
            rots = rots.union(changes)
            time += 1
            
        if time >= maxtime:
            return -1
        return time
        """
        
        
            
            
        