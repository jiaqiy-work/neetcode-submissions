# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            for _ in range(len(queue1)):
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if node1 is None and node2 is None:
                    continue
                    
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                
                queue1.append(node1.left)   
                queue1.append(node1.right)
                queue2.append(node2.left)    
                queue2.append(node2.right)

        return True