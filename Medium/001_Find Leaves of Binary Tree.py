# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Approach One
        leafNodes = []

        def getLeafNodes(root,nodes):
            if root.left is None and root.right is None:
                nodes += [root.val]
                return None
            
            if root.left:
                root.left = getLeafNodes(root.left, nodes)
            
            if root.right:
                root.right = getLeafNodes(root.right, nodes)
                
            return root
        
        while root:
            currentLeaves = []
            root = getLeafNodes(root, currentLeaves)
            leafNodes += [currentLeaves]

        return leafNodes


        # Approach Two
        leafNodesList = []
        def getLeafNodes(root):
            if root is None: return -1

            lHeight = getLeafNodes(root.left)
            rHeight = getLeafNodes(root.right)

            currentHeight = max(lHeight, rHeight) + 1

            if len(leafNodesList) == currentHeight:
                leafNodesList.append([])
            
            leafNodesList[currentHeight].append(root.val)

            return currentHeight

        getLeafNodes(root)
        return leafNodesList



        
        
