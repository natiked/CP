from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n1 = defaultdict(int)
        n2 = {}
        soln = []

        for i in nums1:
            n1[i] += 1
        for i in nums2:
            if i not in n2:
                n2[i] = 1
            else:
                n2[i] += 1

        for key, value in n1.items():
            if key in n2:
                if value < n2[key]:
                    for i in range(value):
                        soln.append(key)
                else:
                    for i in range(n2[key]):
                        soln.append(key)

        return soln






        