#
# @lc app=leetcode.cn id=2413 lang=python3
#
# [2413] 最小偶倍数
#


# @lc code=start
class Solution:

    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            answer = 2 * n
        else:
            answer = n
        return answer


# @lc code=end
