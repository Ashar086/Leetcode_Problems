class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reserved_num = 0
        while x!= 0:
         reserved_num = (reserved_num*10) + (x%10)
         x= x//10
        return original == reserved_num