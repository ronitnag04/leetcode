# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = (self.helper(root))[::-1]
        self.pointer = 0
        self.length = len(self.inorder)
    
    def helper(self, root):
        if not root:
            return []
        order = []
        order.extend(self.helper(root.left))
        order.append(root.val)
        order.extend(self.helper(root.right))
        return order
        
    def next(self) -> int:
        self.pointer += 1
        return self.inorder.pop()
    
    def hasNext(self) -> bool:
        return self.pointer < self.length
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()