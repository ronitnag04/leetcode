class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        def helper(sr, sc, last):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and (sr,sc) not in seen:
                seen.add((sr,sc))
                if image[sr][sc] == last:
                    image[sr][sc] = color
                    
                    nxts = [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]
                    for sr1, sc1 in nxts:
                        helper(sr1, sc1, last)
        helper(sr, sc, image[sr][sc])
        return image
        