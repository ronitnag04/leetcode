class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        holding, changes = 0, [0] * 1001
        for cap, fro, to in trips:
            changes[fro] += cap
            changes[to] -= cap
        for i in range(0, 1001):
            holding += changes[i]
            if holding > capacity:
                return False

        return True
        

        """
        in_car, increase = 0, [0] * 1001
        for [n, fro, to] in trips:  
            increase[fro] += n
            increase[to] -= n
        for i in range(0, 1001):  
            in_car += increase[i]
            if in_car > capacity: return False  
        return True
        """

        """
        froms = {}
        tos = {}
        points = set()

        
        for trip in trips:
            froms[trip[1]] = froms.get(trip[1], []) + [trip]
            points.add(trip[1])
            tos[trip[2]] = tos.get(trip[2], []) + [trip]
            points.add(trip[2])

        holding = 0
        path = sorted(list(points))

        for i in path:
            # s = "at: " + str(i) + " "
            if i in froms.keys():
                pickup = sum([trip[0] for trip in froms[i]])   
                holding += pickup
                # s += "pick: " + str(pickup) + " "
            if i in tos.keys():
                dropoff = sum([trip[0] for trip in tos[i]])
                holding -= dropoff
                # s += "drop: " + str(dropoff) + " "
            # print(s, "holding: ", holding)
            if holding > capacity:
                return False
            
        
        return True
        """


        
        
        
        
        

        