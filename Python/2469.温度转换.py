#
# @lc app=leetcode.cn id=2469 lang=python3
#
# [2469] 温度转换
#

# @lc code=start
from typing import List


class Solution:

    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        ans = [kelvin, fahrenheit]
        return ans


if __name__ == "__main__":
    Answer = Solution()
    print(Answer.convertTemperature(100))
# @lc code=end
