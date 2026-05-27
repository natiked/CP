from collections import defaultdict

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = defaultdict(int)
        n = []
        for j in set(nums1):
            di[j] += 1
        for j in set(nums2):
            di[j] += 1
        for key, value in di.items():
            if value > 1:
                n.append(key)
        return n
