class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s) - 1
        dic = {"(" : 0, "{" : 0, "[" : 0, ")" : 0, "}" : 0, "]":0}
        sta = []

        for i in s:
            dic[i] += 1

        if dic["("] - dic[")"] == 0:
            if dic["{"] - dic["}"] == 0:
                if dic["["] - dic["]"] == 0:
                    for i in range(n):
                        if s[i] == "(" or s[i] == "{" or s[i] == "[":
                            sta.append(s[i])
                        if len(sta) > 0:
                            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                                if s[i] == ")" and sta[-1]=="(":
                                    sta.pop()
                                elif s[i] == "}" and sta[-1]=="{":
                                    sta.pop()
                                elif s[i] == "]" and sta[-1]=="[":
                                    sta.pop()
                                else:
                                    return False
                        else:
                            return False
                    return True
                else:
                     return False
            else:
                 return False
        else:
            return False


        
            
