# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return True, 0

            left_bal, left_height = check(node.left)
            if not left_bal:
                return False, 0

            right_bal, right_height = check(node.right)
            if not right_bal:
                return False, 0

            balanced = abs(left_height - right_height) <= 1
            height = max(left_height, right_height) + 1

            return balanced, height
        
        return check(root)[0]