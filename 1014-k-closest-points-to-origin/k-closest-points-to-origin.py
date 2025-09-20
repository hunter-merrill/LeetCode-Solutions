import math
from collections import defaultdict

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [] # Priority queue (aka heap queue)
        origin = (0,0)
        pointFinder = defaultdict(list) # Find points by hashing their dist

        for point in points:
            distOrigin = math.dist(origin, point)
            heapq.heappush(heap, distOrigin)
            pointFinder[distOrigin].append(point)
        
        kPoints = []
        while len(kPoints) < k:
            for point in pointFinder[heapq.heappop(heap)]:
                kPoints.append(point)
        
        return kPoints