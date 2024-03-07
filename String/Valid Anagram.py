from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t)

    s = "rat"
    t = "car"
    assert solution.isAnagram(s, t) == False
