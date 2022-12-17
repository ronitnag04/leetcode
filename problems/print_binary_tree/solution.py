# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            else:
                return 1 + max(height(root.left), height(root.right))

        def enter(m, row, left, right, root):
            if root:
                col = (left+right)//2
                m[row][col] = str(root.val)
                enter(m, row+1, left, col, root.left)
                enter(m, row+1, col, right, root.right)

        h = height(root)
        matrix = [[""]*(2**(h)-1) for _ in range(h)]
        enter(matrix, 0, 0, len(matrix[0]), root)

        return matrix

        """
        0 1 2 3 4 5 6 _ 8 9 10 11 12 13 14
        0 1 2 _ 4 5 6 7 8 9 10 11 12 13 14
        0 _ 2 3 4 5 6 7 8 9 10 11 12 13 14
        _ 1 2 3 4 5 6 7 8 9 10 11 12 13 14
        """




        """
        if root is None:
            return [[""]]
        if root.left is None and root.right is None:
            return [[str(root.val)]]
        
        leftm = self.printTree(root.left)
        lefth = len(leftm)
        leftw = len(leftm[0])

        rightm = self.printTree(root.right)
        righth = len(rightm)
        rightw = len(rightm[0])

        if leftw < rightw:
            diff = (rightw-leftw)//2
            leftm = [ ["" for i in range(diff)] + 
                       row + 
                       ["" for i in range(diff)] for row in leftm ]
        elif leftw > rightw:
            diff = (leftw-rightw)//2
            rightm = [ ["" for i in range(diff)] + 
                       row + 
                       ["" for i in range(diff)] for row in rightm]
        
        if lefth < righth:
            diff = righth-lefth
            leftm = [row for row in leftm] + [["" for i in range(max(leftw, rightw))] 
                                                for i in range(diff)]

        if lefth > righth:
            diff = lefth-righth
            rightm = [row for row in rightm] + [["" for i in range(max(leftw, rightw))] 
                                                for i in range(diff)]
        
        bottom = [leftr + [""] + rightr for leftr, rightr in zip(leftm, rightm)]
        width = len(bottom[0])
        top = ["" for _ in range(width//2)] + [str(root.val)] + ["" for _ in range(width//2)]

        return top + bottom
        """
