from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        del node

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == "__main__":

    nums = [4,5,1,9]

    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    s = Solution()
    s.deleteNode(head.next)

    while head:
        print(head.val)
        head = head.next