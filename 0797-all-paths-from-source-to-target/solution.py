class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        @lru_cache(None)
        def backtrack(node):
            if node == len(graph) - 1: 
                return [[node]]
            ways = []
            for neigh in graph[node]:
                res = backtrack(neigh)
                for r in res:
                    ways.append([node] + r)
            return ways
        return backtrack(0)