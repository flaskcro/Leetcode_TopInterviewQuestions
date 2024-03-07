from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        answer = []

        i, j = 0, 0
        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            elif sorted_nums1[i] > sorted_nums2[j]:
                j += 1
            else:
                answer.append(sorted_nums1[i])
                i += 1
                j += 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert solution.intersect(nums1, nums2) == [2, 2]

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert solution.intersect(nums1, nums2) == [4, 9]
