class Solution(object):
    def _cycle(self, node):
        if self.visited[node] == 0:
            self.visited[node] = 1
        for nbr in self.adj_list[node]:
            if self.visited[nbr] == 0:
                if self._cycle(nbr):
                    return True
            elif self.visited[nbr] == 1:
                return True
        self.visited[node] = 2
        return False
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.adj_list = []
        self.visited = []
        self.n = numCourses
        for _ in xrange(self.n):
            self.adj_list.append([])
            self.visited.append(0)
        for pair in prerequisites:
            self.adj_list[pair[1]].append(pair[0])
        for node in xrange(self.n):
            if self.visited[node] == 0:
                if self._cycle(node):
                    return False
        return True       
