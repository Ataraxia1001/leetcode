class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        cnt = 0
        for i in range(len(s)/2):
            if s[i] == s[-i-1]:
                continue
            else:
                if cnt >= 1:
                    print('cnt > 1')
                    return False
            
                elif s[i] == s[-i-2]:  
                    cnt += 1
                    s.pop(-i-1)
                    print('pop -i-1')
                    continue
                elif s[i+1] == s[-i-1]:
                    print(cnt)
                    cnt += 1
                    s.pop(i)
                    print('pop i')
                    continue
                else:
                    return False
        return True
    
# 466 / 471 testcases passed