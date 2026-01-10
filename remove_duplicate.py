class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        k = len(seen)
        new_arr = sorted(list(seen))
        for i in range(k):
            nums[i] = new_arr[i]
        return k


        
