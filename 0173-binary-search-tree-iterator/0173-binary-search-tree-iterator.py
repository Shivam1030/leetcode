class BSTIterator:
    st=[]
    def __init__(self, root: Optional[TreeNode]):
        self.pushall(root)

    def next(self) -> int:
        temp=self.st.pop()
        self.pushall(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return True if len(self.st)>0 else False

    def pushall(self,root):
        while root:
            self.st.append(root)
            root=root.left