# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            # Base case
            if node == None:
                return None
            
            # Swap current val of nodes if a val exists
            leftVal = node.left
            rightVal = node.right

            node.left = rightVal
            node.right = leftVal

            # Traverse down tree
            dfs(node.left)
            dfs(node.right)
            return node
        
        return dfs(root)