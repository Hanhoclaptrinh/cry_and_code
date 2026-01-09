class Solution:
    def invertTree(self, root):
        if not root: return None

        #swap left and right
        root.left, root.right = root.right, root.left

        #invert subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root