class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        res = 0
        pre_val = 0
        for i in range(len(s)-1,-1,-1):
            curr_val = dic[s[i]]
            if curr_val >= pre_val:
                res += dic[s[i]]
            else:
                res -= dic[s[i]]
            pre_val = curr_val
        return res             
            

        