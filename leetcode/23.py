link:https://leetcode.com/problems/count-servers-that-communicate/submissions/1518163808/?envType=daily-question&envId=2025-01-23

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        row = [0]*m
        col = [0]*n
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if row[i]>1 or col[j]>1:
                        c+=1
        return c
        