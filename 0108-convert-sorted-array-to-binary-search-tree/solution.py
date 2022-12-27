# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(self, arr):
            if not arr:
                return None
            mid = len(arr)//2
            return TreeNode(arr[mid], helper(self, arr[:mid]), helper(self, arr[mid+1:]))
            
        
        return helper(self, nums)
                