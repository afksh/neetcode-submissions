# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        self.levelOrderHelper(root, 0, result)
        return list(result.values())
    
    def levelOrderHelper(self, node: Optional[TreeNode], level: int, result: dict[int, list[int]]):
        if node:
            result[level].append(node.val)
            self.levelOrderHelper(node.left, level + 1, result)
            self.levelOrderHelper(node.right, level + 1, result)
        return result
