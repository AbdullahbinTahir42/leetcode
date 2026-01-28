class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        new_sum = 0

        for i in range(len(nums)):
            if (total_sum - nums[i]) == (new_sum * 2):
                return i 

            new_sum += nums[i]
        return -1

        
