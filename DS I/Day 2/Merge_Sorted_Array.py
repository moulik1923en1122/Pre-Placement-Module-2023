class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while 0 in nums1 and len(nums1) > m:
            nums1.remove(0)
        nums1.extend(nums2)
        nums1.sort()