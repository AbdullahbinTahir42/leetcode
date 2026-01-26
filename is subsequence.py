class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_p,t_p = 0,0
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False 
        else:
            while  s_p < len(s) and t_p < len(t):
                if s[s_p] == t[t_p]:
                    s_p += 1  
                    t_p += 1  
                else:
                    t_p += 1
            
        return True if len(s) == s_p else False
        
