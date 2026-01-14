class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        l1, l2 = len(str1),len(str2)
        gcd = 1
        for i in range(1,min(l1,l2) + 1):
            if l1 % i == 0 and l2 % i == 0:
                gcd = i
        return str1[:gcd]

