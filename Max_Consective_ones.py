class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        max = 0
        for num in nums:
            if num == 1:
                n += 1
            elif num == 0:
                if n > max:
                    max = n
                    n = 0
                else:
                    n = 0
            else:
                return 0
        if n > max:
            max = n
        return max

