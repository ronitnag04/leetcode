class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        """ Not Time Efficient
        if len(matrix) == 1:
            return matrix[0][0]
        
        total = 100000000000
        def fallCheck(r, c):
            if r == len(matrix) - 1 :
                return matrix[r][c]
            if c >= len(matrix[0]) or c < 0:
                return 10000000000
            if (c == 0):
                return matrix[r][c] + min(fallCheck(r+1, c), fallCheck(r+1, c+1))
            if (c == len(matrix[0])-1):
                return matrix[r][c] + min(fallCheck(r+1, c), fallCheck(r+1, c-1))
            return matrix[r][c] + min(fallCheck(r+1, c), fallCheck(r+1, c-1), fallCheck(r+1, c+1))
            
            
            
            
        for c in range(len(matrix[0])):
            total = min(total, fallCheck(0, c))
        
        return total
        """
        if len(matrix) == 1:
            return matrix[0][0]
        
        newMatrix = []
        for r in range(len(matrix)):
            newarr = []
            for c in range(len(matrix)):
                newarr.append(0)
            newMatrix.append(newarr)
                

        newMatrix[0] = matrix[0]
        for r in range(1, len(matrix)):
            for c in range(len(matrix[r])):
                if (c == 0):
                    newMatrix[r][c] = matrix[r][c] + min(newMatrix[r-1][c], newMatrix[r-1][c+1])
                elif (c == len(matrix[0])-1):
                    newMatrix[r][c] = matrix[r][c] + min(newMatrix[r-1][c], newMatrix[r-1][c-1])
                else:
                    newMatrix[r][c] = matrix[r][c] + min(newMatrix[r-1][c], newMatrix[r-1][c-1], newMatrix[r-1][c+1])
        
        return min(newMatrix[len(matrix)-1])
        
        
        