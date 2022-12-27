# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(self, root):
            if not root:
                return []
            order = []
            order.extend(helper(self, root.left))
            order.append(root.val)
            order.extend(helper(self, root.right))
            return order
        
        return helper(self, root)[k-1]
        
        