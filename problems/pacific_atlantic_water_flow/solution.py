class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # O(n) time O(1) memory
        y = len(heights)
        x = len(heights[0])
        
        def recur(i, j, prevh, cor):
            if (i, j) not in cor:
                if 0 <= i < y and 0 <= j < x:
                    h = heights[i][j]
                    if h >= prevh:
                        cor.add((i,j))
                        recur(i+1, j  , h, cor)
                        recur(i-1, j  , h, cor)
                        recur(i  , j+1, h, cor)
                        recur(i  , j-1, h, cor)
        
        pacifics = set()
        atlantics = set()
        
        for col in range(x):
            recur(0, col, 0, pacifics)
        for row in range(y):
            recur(row, 0, 0, pacifics)
            
        for col in range(x-1, -1, -1):
            recur(y-1, col, 0, atlantics)
        for row in range(y):
            recur(row, x-1, 0, atlantics)
        
        return atlantics.intersection(pacifics)
                
        
        
        
        
        
        
        """
        # O(n) time  O(n) memory
        pacifics = [[False for _ in range(x)] for _ in range(y)]
        atlantics = [[False for _ in range(x)] for _ in range(y)]
        pacifics[0] = [True for _ in range(x)]
        for row in range(y):
            pacifics[row][0] = True
            atlantics[row][-1] = True
        atlantics[y-1] = [True for _ in range(x)]
        
        
        pacificChecks .....
        
                            
        [print(pacifics[row]) for row in range(y)]
        print()
        [print(atlantics[row]) for row in range(y)]
        
        
        #O(n) time O(n) memory
        reachable = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if pacifics[row][col] and atlantics[row][col]:
                    reachable.append([[row, col]])
        return reachable
        """