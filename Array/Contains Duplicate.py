from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    assert solution.containsDuplicate(nums)

    nums = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums) == False

    nums = [1,1,1,3,3,4,3,2,4,2]
    assert solution.containsDuplicate(nums)
