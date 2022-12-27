class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        
        taken = set()
        path = []
        while prereqs:
            term = [key for key in prereqs.keys() 
                    if [course for course in prereqs[key] if course not in taken]==[]]
            if not term:
                return term
            for t in term:
                taken.add(t)
                del prereqs[t]
            path.extend(term)
        return path
        
        
        
        
        
        