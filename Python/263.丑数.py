#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#


# @lc code=start
class Solution:

    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        factors = set()
        if n <= 1:
            return True

        # 处理2作为质因数的情况
        while n % 2 == 0:
            factors.add(2)
            n //= 2

        # 从3开始，检查所有奇数
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                factors.add(factor)
                n //= factor
            factor += 2

        # 如果n本身是一个大于2的质数
        if n > 1:
            factors.add(n)

        allowed_elements = (2, 3, 5)
        if factors.issubset(allowed_elements):
            return True
        else:
            return False


# @lc code=end
