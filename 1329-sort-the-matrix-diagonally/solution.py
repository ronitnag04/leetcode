class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sortDiagonal(i, j):
            r = i
            c = j
            diag = []
            while i < len(mat) and j<len(mat[i]):
                diag.append(mat[i][j])
                i += 1
                j += 1
            diag.sort()
            for e in diag:
                mat[r][c] = e
                r += 1
                c += 1
        for j in range(len(mat[0])):
            sortDiagonal(0, j)
        for r in range(1, len(mat)):
            sortDiagonal(r, 0)
        
        return mat
        
        
        """
        def getDiagonal(i, j):
            diag = []
            while i < len(mat) and j<len(mat[i]):
                diag.append(mat[i][j])
                i += 1
                j += 1
            return sorted(diag)
        
        diags1 = []
        for j in range(len(mat[0])):
            diags1.append(getDiagonal(0, j))

        diags2 = []
        for r in range(1, len(mat)):
            diags2.append(getDiagonal(r, 0)) 
        
        
        c = 0
        for diag in diags1:
            i = 0
            j = c
            for e in diag:
                mat[i][j] = e
                i += 1
                j += 1
            c += 1
        
        r = 1
        for diag in diags2:
            i = r
            j = 0
            for e in diag:
                mat[i][j] = e
                i += 1
                j += 1
            r += 1

        return mat
        """

        