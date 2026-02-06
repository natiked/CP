class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not(needle in haystack):
            return -1
        else:
            n = len(needle)
            m = len(haystack)
            if m == 1:
                return 0
            for i in range(0,m):
                if haystack[i:n] == needle:
                    return i
                if n<=m:
                    n+=1

        