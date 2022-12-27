class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper = 0
        lower = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        
        path = []
        direction = 1
        """
           1
        4 -|- 2
           3
        """
        while (left <= right) and (upper <= lower) :
            if direction == 1:
                path.extend(matrix[upper][left:right+1])
                direction = 2
                upper += 1
            elif direction == 2:
                path.extend([matrix[r][right] for r in range(upper, lower+1)])
                direction = 3
                right-=1
            elif direction == 3:
                path.extend(matrix[lower][left:right+1][::-1])
                direction = 4
                lower -= 1
            elif direction == 4:
                path.extend([matrix[r][left] for r in range(upper, lower+1)][::-1])
                direction = 1
                left += 1
        return path          
            
                    
            
        