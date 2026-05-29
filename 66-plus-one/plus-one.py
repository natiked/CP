class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join(map(str, digits)))
        x += 1
        y = list(map(int, str(x)))
        return y
        