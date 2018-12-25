class Solution(object):
    def is_safe(self, r, c):
        return r >= 0 and r < self.m and c >= 0 and c < self.n
    
    def DFS(self, r, c):
        self.visited[r][c] = True
        nbrs = [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]
        for i, j in nbrs:
            if self.is_safe(i,j) and self.grid[i][j] == "1" and not self.visited[i][j]:
                self.DFS(i,j)
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid:
            self.grid = grid
            self.m  = len(grid)
            self.n = len(grid[0])
            self.visited = []
            for _ in xrange(self.m):
                inner = []
                for _ in xrange(self.n):
                    inner.append(False)
                self.visited.append(inner)
            count = 0
            for r in xrange(self.m):
                for c in xrange(self.n):
                    if self.grid[r][c] == "1" and not self.visited[r][c]:
                        self.DFS(r,c)
                        count += 1
            return count            
        else:
            return 0
