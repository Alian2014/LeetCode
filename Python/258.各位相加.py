#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#


# @lc code=start
class Solution:

    def addDigits(self, num: int) -> int:
        import math

        while num >= 10:
            if num == 0:
                return 0
            digit_count = math.floor(math.log10(abs(num))) + 1
            sum = 0
            for i in range(digit_count):
                single_num = num % 10
                sum += single_num
                num -= single_num
                num //= 10
            num = sum
        return num


if __name__ == '__main__':
    Answer = Solution()
    print(Answer.addDigits(38))

# @lc code=end
