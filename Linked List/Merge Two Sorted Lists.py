from typing import Optional
from ListNode import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode(0)
        node = head

        while list1 and list2:
            new_node = None

            if list1.val < list2.val:
                new_node = ListNode(list1.val)
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                list2 = list2.next

            node.next = new_node
            node = node.next

        if list1:
            node.next = list1

        if list2:
            node.next = list2

        return head.next

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 4]

    head1 = ListNode(nums[0])
    node = head1
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    nums = [1, 3, 4]
    head2 = ListNode(nums[0])
    node = head2
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    answer = [1,1,2,3,4,4]
    result = solution.mergeTwoLists(head1, head2)
    while result:
        count = 0
        while result:
            assert result.val == answer[count]
            result = result.next
            count += 1