class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        tmp = intervals[0]
        for n in intervals[1:] :
            if n[0] < tmp[1] :
                res += 1
                if tmp[1] > n[1] :
                    tmp = n
            else :
                tmp = n
        return res