class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        indicies = [row[0] for row in matrix]
        i = 0
        while i+1 < len(matrix) and target >= indicies[i+1]:
            i += 1
        return target in matrix[i]
        
        