class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        d = {}
        for task in tasks:
            d[task] = 1 + d.get(task, 0)
            time += 1
        while d:
            cycle = n+1
            stillTasks = list(d.keys())
            while cycle and stillTasks:
                cycle -= 1
                key = max(stillTasks, key=lambda x:d[x])
                stillTasks.pop(stillTasks.index(key))
                if d[key] == 1:
                    del d[key]
                else:
                    d[key] -= 1
            if d:
                time += cycle
            else:
                return time
            
        
        
            