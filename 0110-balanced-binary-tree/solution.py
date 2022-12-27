# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        @lru_cache(None)
        def getHeight(root):
            if not root:
                return 0
            l = getHeight(root.left)
            r = getHeight(root.right)
            if r==-1 or l==-1 or abs(r-l)>1:
                return -1
            else:
                return 1+ max(l,r)
        
        if not root:
            return True

        
        return getHeight(root) != -1