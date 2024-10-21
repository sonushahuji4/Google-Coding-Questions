# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:

        startPaths = []
        destinationPaths = []

        def find(root, target, paths):
            
            if root is None: return False
            if root.val == target: return True
            
            paths.append("L")
            leftPath = find(root.left, target, paths)
            if leftPath: return True
            paths.pop()

            paths.append("R")
            rightPath = find(root.right, target, paths)
            if rightPath: return True
            paths.pop()

            return False

        find(root, startValue, startPaths)
        find(root, destValue, destinationPaths)

        directions, commonPathLength = [], 0
        startPathLength, destinationPathLength = len(startPaths), len(destinationPaths)
        while commonPathLength < startPathLength and commonPathLength < destinationPathLength and startPaths[commonPathLength] == destinationPaths[commonPathLength]:
            commonPathLength += 1
        
        directions.extend("U" * (startPathLength - commonPathLength))
        directions.extend(destinationPaths[commonPathLength:])

        return "".join(directions)
