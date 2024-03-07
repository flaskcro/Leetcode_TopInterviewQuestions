from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


if __name__ == "__main__":
    solution = Solution()
    s = ["h","e","l","l","o"]
    solution.reverseString(s)
    assert s == ["o","l","l","e","h"]

    s = ["H","a","n","n","a","h"]
    solution.reverseString(s)
    assert s == ["h","a","n","n","a","H"]