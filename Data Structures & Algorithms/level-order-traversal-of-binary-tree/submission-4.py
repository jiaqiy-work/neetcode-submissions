# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        dq = collections.deque()
        dq.append(root)

        while dq:
            qLen = len(dq)
            level = []
            for i in range(qLen):
                node = dq.popleft()
                if node: 
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if level: 
                res.append(level)
        return res
