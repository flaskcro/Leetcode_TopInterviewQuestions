from typing import Optional
from ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        return arr[:] == arr[::-1]


if __name__ == "__main__":
    nums = [1,2,2,1]
    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    s = Solution()
    assert s.isPalindrome(head)

