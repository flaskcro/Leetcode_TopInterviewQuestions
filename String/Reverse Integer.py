from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        start = 0
        x = str(x)
        is_negative = False
        if x[0] == '-':
            is_negative = True
            start = 1

        for i in range(len(x) - 1, start - 1, -1):
            temp = int(x[i]) * 10 ** (i - start)
            answer += temp

        if is_negative:
            answer *= -1

        if answer > 2 ** 31 - 1 or answer < -2 ** 31:
            return 0

        return answer


if __name__ == "__main__":
    solution = Solution()
    x = 123
    assert solution.reverse(x) == 321

    x = -123
    assert solution.reverse(x) == -321

    x = 120
    assert solution.reverse(x) == 21
