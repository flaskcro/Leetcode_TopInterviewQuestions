from ListNode import ListNode


class Solution:
    def deleteNode(self, node):
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next
        nextNode.next = None
        del (nextNode)


if __name__ == "__main__":

    nums = [4,5,1,9]

    head = ListNode(nums[0])
    node = head
    for i in nums[1:]:
        node.next = ListNode(i)
        node = node.next

    s = Solution()
    s.deleteNode(head.next.next)

    while head:
        print(head.val)
        head = head.next