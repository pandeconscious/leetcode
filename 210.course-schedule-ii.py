class Solution:
    def topoSort(self, node):
        for nbr in self.adj_list[node]:
            if self.visited[nbr] == 'G':
                return False
            if self.visited[nbr] == 'B':
                continue
            self.visited[nbr] = 'G'
            topo_success = self.topoSort(nbr)
            if not topo_success:
                return False
            self.visited[nbr] = 'B'
            self.ordering.append(nbr)
        return True
                
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.ordering = []
        self.adj_list = [[] for _ in range(numCourses)]
        self.visited = ['W' for _ in range(numCourses)]
        for edge in prerequisites:
            self.adj_list[edge[1]].append(edge[0])
        
        for node in range(numCourses):
            if self.visited[node] == 'G':
                return []
            if self.visited[node] == 'B':
                continue
            self.visited[node] = 'G'
            topo_success = self.topoSort(node)
            if not topo_success:
                return []
            self.visited[node] = 'B'
            self.ordering.append(node)
        
        return self.ordering[::-1]
        
