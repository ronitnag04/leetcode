class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = {n:set() for n in range(1, n+1)}
        for x, y in paths:
            graph[x].add(y)
            graph[y].add(x)
            
        flower = [0 for n in range(n)]
        
        for garden, neighbors in graph.items():
            nflowers = [flower[n-1] for n in neighbors]
            options = [n for n in [1, 2, 3, 4] if n not in nflowers]
            flower[garden-1] = options[0]
        
        return flower
            
            