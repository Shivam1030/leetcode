# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fxn(root, temp):
            if not root:
                return False

            temp += root.val

            if not root.left and not root.right:
                return temp == targetSum

            return fxn(root.left, temp) or fxn(root.right, temp)

        return fxn(root, 0)