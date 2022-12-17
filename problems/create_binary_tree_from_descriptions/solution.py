# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = set()
        childs = set()


        for parent, child, side in descriptions:
            parents.add(parent)
            childs.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            if side == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        head = set.difference(parents, childs).pop()
        return nodes[head]