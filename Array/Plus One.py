from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        remains = 1
        answer = [0 for _ in range(len(digits))]
        for i in range(len(digits) - 1, -1, -1):
            num = (digits[i] + remains) % 10
            remains = (digits[i] + remains) // 10

            answer[i] = num
        if remains == 1:
            answer.insert(0, 1)

        return answer


if __name__ == "__main__":
    solution = Solution()
    digits = [4, 3, 2, 1]
    assert solution.plusOne(digits) == [4,3,2,2]

    digits = [9]
    assert solution.plusOne(digits) == [1,0]

    digits = [9,9,9]
    assert solution.plusOne(digits) == [1,0,0,0]