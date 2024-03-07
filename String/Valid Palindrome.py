from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = []
        for c in s:
            if c.isalnum():
                answer.append(c.lower())

        return answer == answer[::-1]


if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    assert solution.isPalindrome(s)

    s = "race a car"
    assert solution.isPalindrome(s) == False

    s = " "
    assert solution.isPalindrome(s)
