from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap and hashmap[target - nums[i]] != i:
                return [i, hashmap[target - nums[i]]]


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert solution.twoSum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert solution.twoSum(nums, target) == [0, 1]