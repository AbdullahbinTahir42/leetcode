class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank_map = {}
        
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num not in rank_map:
                rank_map[num] = i
                
        result = []
        for num in nums:
            result.append(rank_map[num])
            
        return result
