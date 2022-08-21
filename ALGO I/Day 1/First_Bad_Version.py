class Solution:
    def firstBadVersion(self, n: int) -> int:
        start,end = 1,n
        while start<end:
            mid = start+(end-start)//2
            res = isBadVersion(mid)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start