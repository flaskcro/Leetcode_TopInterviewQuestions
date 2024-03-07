from typing import List
"""
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements 
in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                pass
            else:
                nums[count] = nums[i]
                count += 1
                prev = nums[i]
        for i in range(count, len(nums)):
            nums[i] = '_'

        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    assert solution.removeDuplicates(nums) == 2

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solution.removeDuplicates(nums) == 5
