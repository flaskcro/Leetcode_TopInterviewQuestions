from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        for key in counter.keys():
            if counter[key] == 1:
                return key


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 1]
    assert solution.singleNumber(nums) == 1

    nums = [4, 1, 2, 1, 2]
    assert solution.singleNumber(nums) == 4

    nums = [1]
    assert solution.singleNumber(nums) == 1
