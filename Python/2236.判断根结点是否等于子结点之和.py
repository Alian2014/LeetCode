#
# @lc app=leetcode.cn id=2236 lang=python3
#
# [2236] 判断根结点是否等于子结点之和
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False


# @lc code=end
