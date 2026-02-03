class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        listStr = s.split()
        return len(listStr[-1])