class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        strXRev = strX[len(strX)-1::-1]
        if strX == strXRev:
            return True
        else:
            return False