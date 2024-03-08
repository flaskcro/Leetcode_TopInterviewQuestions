from typing import Optional
from ListNode import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    answer = [5, 4, 3, 2, 1]

    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    s = Solution()
    reverse_head = s.reverseList(head)

    count = 0
    while reverse_head:
        assert reverse_head.val == answer[count]
        reverse_head = reverse_head.next
        count += 1