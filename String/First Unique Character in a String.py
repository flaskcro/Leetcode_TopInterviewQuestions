from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        coutner = Counter(s)

        for i in range(len(s)):
            if coutner[s[i]] == 1:
                return i
        return - 1


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    assert solution.firstUniqChar(s) == 0

    s = "loveleetcode"
    assert solution.firstUniqChar(s) == 2

    s = "aabb"
    assert solution.firstUniqChar(s) == -1
