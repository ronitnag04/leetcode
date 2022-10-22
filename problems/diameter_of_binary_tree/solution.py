# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, found, height):
            if not root:
                return 0, height-1
            
            lf, lh = helper(root.left, found, height+1)
            rf, rh = helper(root.right, found, height+1)
            
            path = (lh-height)+(rh-height)
            return max(path, found, lf, rf), max(lh, rh)
            
            
                
            
            
            
        return helper(root, 0, 0)[0]
            
        