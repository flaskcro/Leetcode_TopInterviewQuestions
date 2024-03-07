from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    assert solution.strStr(haystack, needle) == 0

    haystack = "leetcode"
    needle = "leeto"
    assert solution.strStr(haystack, needle) == -1