# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/

class UnionFindBySize:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU == rootV: return False

        if self.size[rootU] < self.size[rootV]:
            self.parent[rootU] = rootV
            self.size[rootV] += self.size[rootU]
        else:
            self.parent[rootV] = rootU
            self.size[rootU] += self.size[rootV]
            
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])

        uf = UnionFindBySize(n)
        groupCnt = n

        for timestamp, friendA, friendB in logs:
            if uf.union(friendA, friendB):
                groupCnt -= 1

            if groupCnt == 1: return timestamp
        
        return -1
