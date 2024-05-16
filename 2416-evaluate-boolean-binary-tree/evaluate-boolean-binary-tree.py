class Solution(object):
    def evaluateTree(self, root):
        # Base condition, if it's a leaf node
        if not root.left and not root.right:
            if root.val == 0:
                return False
            return True
        # If it's not a leaf node, then go to left subtree
        left = self.evaluateTree(root.left)
        # then go to right subtree
        right = self.evaluateTree(root.right)
        # OR operation
        if root.val == 2:
            return left or right
        return left and right  # AND operation