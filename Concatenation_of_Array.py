class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        if n > 0 and n <= 1000:
            for i in range(0,len(nums),1):
                ans[i] = nums[i]
                ans[i + n] = nums[i]
        else:
            print("Lenght should be between 1 and 1000")
        return ans
        
