class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        def dfs(city):
            if city not in visited:
                visited.add(city)
                for i in range(len(isConnected)):
                    if isConnected[i][city] == 1:
                        dfs(i)
        
        provs = 0
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provs += 1
        
        return provs
        