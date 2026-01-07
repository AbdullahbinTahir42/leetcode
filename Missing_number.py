class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        actual_sum = sum(nums)
        expected_sum = 0
        for i in range(1,len(nums)+1):
            expected_sum += i
        return expected_sum-actual_sum
