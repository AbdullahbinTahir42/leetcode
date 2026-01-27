class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        arr_set = set()
        for num in arr:
            try:
                dict[num] += 1
            except KeyError:
                dict[num] = 1

        for value in dict.values():
            if value in arr_set:
                return False
            arr_set.add(value)
        return True 


        
