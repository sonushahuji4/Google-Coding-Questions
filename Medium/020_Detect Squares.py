# https://leetcode.com/problems/detect-squares/description/

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.points_count = defaultdict(int)

    def add(self, point):
        # Increment the count for the given point
        x, y = point
        self.points_count[(x, y)] += 1

    def count(self, point):
        qx, qy = point
        square_count = 0

        # Loop through points to find potential squares
        for (px, py), freq in self.points_count.items():
            # Check if point and query point are aligned in the x or y axis
            if abs(px - qx) == abs(py - qy) and px != qx and py != qy:
                # We now have potential points forming a square
                p2 = (px, qy)  # Point along the horizontal line with q
                p3 = (qx, py)  # Point along the vertical line with q

                # Multiply counts of each point to get total configurations
                square_count += (freq * 
                                 self.points_count.get(p2, 0) *
                                 self.points_count.get(p3, 0))
        
        return square_count
