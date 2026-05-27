class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = sum(nums)
        n = len(nums)
        y = (n * (n+1))/2
        return abs(int(x - y))
        