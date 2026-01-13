class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_val = min(len(word1),len(word2))
        result = []
        for i in range(min_val):
            result.append(word1[i]) 
            result.append(word2[i])

        if len(word1) > len(word2):
            result.append(word1[min_val:])
        else:
            result.append(word2[min_val:])

        
        return "".join(result)  
        
