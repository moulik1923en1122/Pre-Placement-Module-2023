from math import pow
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i in range(len(points)) :
            dis.append([pow(points[i][0],2)+pow(points[i][1],2),points[i]])
        heapq.heapify(dis)
        smallest = heapq.nsmallest(k,dis)
        return [p[1] for p in smallest]