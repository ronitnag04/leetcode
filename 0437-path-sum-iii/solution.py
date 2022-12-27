# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def getSums(self, root):
            if root is None:
                return []
            left = getSums(self, root.left)
            right = getSums(self, root.right)
            sums = left + right
            sums = [s+root.val for s in sums]
            sums.append(root.val)
            self.match += sums.count(targetSum)
            return sums
        
        self.match = 0
        getSums(self, root)
        
        return self.match
        
        
    """   
                    10
            5               -3
        3       2                11
      3  -2       1
    
    
    [10, 15, 18, 21, 16, 17, 18, 7, 18]
                    
    [5, 8, 11, 6, 7, 8]          [-3, 8]
    [3,6,1]     [2, 3]              11
    3    -2         1
        """