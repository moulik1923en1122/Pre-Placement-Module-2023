class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1) & Counter(nums2)
        res = []
        for i in counts.elements():
            res.append(i)
        return res
        