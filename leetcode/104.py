class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # neu cay rong thi do sau la 0
        if not root:
            return 0
        
        # de quy tinh do sau cua cay con trai va cay con phai
        leftd = self.maxDepth(root.left)
        rightd = self.maxDepth(root.right)

        # tra ve do sau lon nhat cua hai cay con cong voi 1 (node hien tai)
        return max(leftd, rightd) + 1