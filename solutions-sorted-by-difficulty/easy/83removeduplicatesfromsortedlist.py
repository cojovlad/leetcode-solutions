class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)

elements = [1, 2, 2, 3]
head = create_linked_list(elements)
solution = Solution()
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head)
