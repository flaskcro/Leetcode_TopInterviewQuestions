from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(n) for n in strs])
        answer = ""

        for i in range(min_len):
            p = strs[0]
            for l in strs[1:]:
                if p[i] != l[i]:
                    return answer
            answer += p[i]

        return answer


if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    assert solution.longestCommonPrefix(strs) == "fl"

    strs = ["dog","racecar","car"]
    assert solution.longestCommonPrefix(strs) == ""
