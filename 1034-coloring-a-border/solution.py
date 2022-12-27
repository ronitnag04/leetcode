class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        comp = grid[row][col]
        border = set()
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        def dfs(row, col):
            if (row, col) not in seen:
                seen.add((row, col))
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == comp:
                    if row == 0 or row == rows-1 or col == 0 or col == cols-1:
                        border.add((row, col))
                    elif (grid[row+1][col]!=comp or grid[row-1][col]!=comp or grid[row][col+1]!=comp or grid[row][col-1]!=comp):
                        border.add((row, col))
                    dfs(row-1, col)
                    dfs(row+1, col)
                    dfs(row, col-1)
                    dfs(row, col+1)
        dfs(row, col)
        for row, col in border:
            grid[row][col] = color
        return grid
                
                
        
            
            
        
        