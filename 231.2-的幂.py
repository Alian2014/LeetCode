#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#


# @lc code=start
class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        g = 1
        if g == n:
            return True
        while g != n:
            g = g * 2
            if n < g:
                return False
            elif n % g != 0:
                return False
        return True


# @lc code=end
