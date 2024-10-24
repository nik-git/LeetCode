class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        temp = x
        while temp:
            rev = rev * 10 + temp % 10
            print(rev)
            temp = temp // 10
        return rev == x

print(Solution().isPalindrome(121))
