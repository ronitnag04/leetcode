class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rlength = len(grid[0])
        
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[row])):
                nextCol = col + grid[row][col]
                if 0 <= nextCol < rlength and grid[row][col] == grid[row][nextCol]:
                    if row == len(grid)-1:
                        dp[row][col] = nextCol
                    else:
                        dp[row][col] = dp[row+1][nextCol]
                else:
                    dp[row][col] = -1                       
                        
                        
        return dp[0]
                
        """
        left = -1
        right = len(grid[0])
        bottom = len(grid)
        
        def getPath(row, col):
            if row == bottom:
                return col
            
            if grid[row][col] == 1:
                if col+1 == right or grid[row][col+1] == -1:
                    return -1
                return getPath(row+1, col+1)
            else:
                if col-1 == left or grid[row][col-1] == 1:
                    return -1
                return getPath(row+1, col-1)
        
        return [getPath(0, i) for i in range(right)]
        """