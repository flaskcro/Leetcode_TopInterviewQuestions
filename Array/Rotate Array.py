"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)
    assert nums == [3,99,-1,-100]
