class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_arr = []
        for num in nums:
            if num != val:
                new_arr.append(num)
        k = len(new_arr)
        for i in range(k):
            nums[i] = new_arr[i]
        return k
        
