# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(original, cloned, target):
            if original is None or cloned is None:
                return False
            elif original == target:
                return cloned
            else:
                left = helper(original.left, cloned.left, target)
                right = helper(original.right, cloned.right, target)
                return left or right
        return helper(original, cloned, target)
            