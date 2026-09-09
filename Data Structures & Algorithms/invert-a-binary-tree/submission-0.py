# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        que=[root]
        while(que):
            ele=que.pop(0)
            ele.left,ele.right=ele.right,ele.left
            if ele.left:
                que.append(ele.left)
            if ele.right:
                que.append(ele.right)
        return root


        