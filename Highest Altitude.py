class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        max = 0
        for g in gain:
            total += g
            if total > max:
                max = total
        
        return max
