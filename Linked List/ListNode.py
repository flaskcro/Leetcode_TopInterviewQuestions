class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def make_linked_list(arr):
        head = ListNode(arr[0])
        node = head
        for n in arr[1:]:
            node.next = ListNode(n)
            node = node.next
        return head

if __name__ == '__main__':
    head = ListNode.make_linked_list(list(range(1, 11)))
    while head:
        print(head.val)
        head = head.next