class bt:
    def __init__(self, data):
        self.data= data
        self.lc = None
        self.rc = None
def insert(root, newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue>root.data:
        root.lc=insert(root.lc, newvalue)
    else:
        root.rc=insert(root.rc, newvalue)
    return root
def inorder(root):
    if root == None:
        return
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
root = insert(None, 15)
insert(root, 10)
insert(root, 24)
insert(root, 5)
insert(root, 14)
insert(root, 22)
insert(root, 55)
insert(root, 98)
print("Inorder traversal of a bst")
inorder(root)
