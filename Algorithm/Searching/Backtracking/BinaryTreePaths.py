# -*- coding: UTF-8 -*-

'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: # TODO: 复习
    def binaryTreePaths(self, root):
        output = []
        def dfs(root, combination):
            if root:
                combination += str(root.val)
                if not root.left and not root.right:
                    output.append(combination)
                else:
                    combination += '->'
                    dfs(root.left, combination)
                    dfs(root.right, combination)

        dfs(root, '')
        return output


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths


# if __name__ == '__main__':
#     print(Solution().binaryTreePaths([1,2,3,'null',5]))