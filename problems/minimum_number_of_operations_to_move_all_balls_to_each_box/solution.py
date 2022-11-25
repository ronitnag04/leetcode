class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        posBalls = []

        balls = 0
        left = 0
        for i, char in enumerate(boxes):
            posBalls.append(left)
            left += balls
            if char == '1':
                balls += 1
                left += 1
        
        balls = 0
        right = 0
        for i in range(len(boxes)-1, -1, -1):
            posBalls[i] += right
            right += balls
            if boxes[i] == '1':
                balls += 1
                right += 1
            
        return posBalls
