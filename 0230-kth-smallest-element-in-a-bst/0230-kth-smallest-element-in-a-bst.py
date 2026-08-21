class Solution:
    def kthSmallest(self, root, k):
        result = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result[k - 1]
        