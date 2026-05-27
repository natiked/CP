class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sma = 0
        mini = len(strs[0])

        for i in range(len(strs)):
            if len(strs[i]) < mini:
                mini = len(strs[i])
                sma = i

        shortest = strs[sma]

        j = 0
        while j < len(shortest):

            for i in range(len(strs)):
                if strs[i][j] != shortest[j]:
                    return shortest[:j]

            j += 1

        return shortest