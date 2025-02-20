class Solution: #reverse number method
    def isPalindrome(self, x: int) -> bool:
        new = 0
        old = x
        while x > 0:
            r = x % 10
            new = (new * 10) + r
            x = x // 10

        if old == new:
            return True
        return False


        