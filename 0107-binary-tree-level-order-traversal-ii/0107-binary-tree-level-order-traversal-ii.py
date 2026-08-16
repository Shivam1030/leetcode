class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node, lvl):
            if not node:
                return
            
            # If we are visiting this level for the first time, create a new list for it
            if lvl == len(ans):
                ans.append([])
                
            # Add the current node's value to its corresponding levels list
            ans[lvl].append(node.val)
            
            # Traverse left and right, increasing the level by 1
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
            
        dfs(root, 0)
        
        # Return the reversed list (Python slice notation)
        return ans[::-1] 