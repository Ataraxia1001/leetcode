class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_lis = []
        t_lis = []
        for i in range(len(s)):
            if t[i] in t_lis and s[i] not in s_lis: # and s[i] not in s_lis
                print(s[i], t[i])
                return False
            elif s[i] in s_lis and t[i] not in t_lis:
                return False
            elif s[i] in s_lis and t[i] in t_lis and s[i] == t[i]:
                return False
            else:
                s_lis.append(s[i])
                t_lis.append(t[i])
                print(s[i])
                print(t[i])
                s = s[:i] + t[i] + s[i+1:]
                
        print(s)
        if s == t: 
            return True
        else:
            return False

# 38 / 45 testcases passed.