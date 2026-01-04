class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        # neu la cay rong thi luon doi xung
        if not root:
            return True

        def isMirror(t1, t2):
            # ca 2 deu rong => doi xung
            if not t1 and not t2:
                return True

            # 1 trong 2 null hoac co gia tri khac nhau => khong doi xung
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # cross check
            return isMirror(t1.left,t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root.left, root.right)