class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n<3:return n
        ma=0
        for i in range(n):
            x1,y1=points[i]
            d=defaultdict(int)
            for j in range(i+1,n):
                x2,y2=points[j]
                slope=(y2-y1)/(x2-x1) if x1!=x2 else inf
                d[slope]+=1
                ma=max(d[slope],ma)
        return ma+1
