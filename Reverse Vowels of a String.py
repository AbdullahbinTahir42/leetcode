class Solution:
    def reverseVowels(self, s: str) -> str:
        x1, x2 = 0, len(s) - 1
        vowels = set("aeiouAEIOU")
        lists = list(s)
        while x2 > x1:
            if (lists[x1] in vowels) and (lists[x2] in vowels):
                lists[x1],lists[x2] = lists[x2], lists[x1]
                x1 += 1
                x2 -= 1
            elif (lists[x2] not in vowels) and (lists[x1] in vowels):
                x2 -= 1
            elif (lists[x1] not in vowels) and (lists[x2] in vowels):
                x1 += 1
            else:
                x1 += 1
                x2 -= 1

        s = "".join(lists)
        return s


        
