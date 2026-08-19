# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def backtrack(curr, sol, curr_sum):
            if curr is not None:
                sol.append(curr.val)
                curr_sum += curr.val
                if curr.left is None and curr.right is None and curr_sum == targetSum:
                    res.append(sol[:])
                if curr.left:
                    backtrack(curr.left, sol, curr_sum)
                if curr.right:
                    backtrack(curr.right, sol, curr_sum)
                sol.pop()

        backtrack(root, [], 0)
        return res