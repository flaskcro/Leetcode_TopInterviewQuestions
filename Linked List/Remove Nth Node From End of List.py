from typing import Optional
from ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        psuedo_head = ListNode(0)
        psuedo_head.next = head

        count = 0
        while head:
            head = head.next
            count += 1

        head = psuedo_head
        for i in range(count - n):
            head = head.next

        head.next = head.next.next

        return psuedo_head.next


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5]

    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    s = Solution()
    head = s.removeNthFromEnd(head, 2)

    while head:
        print(head.val)
        head = head.next
