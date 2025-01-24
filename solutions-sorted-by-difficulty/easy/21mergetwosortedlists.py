class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        temp = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        temp.next = list1 or list2

        return dummy.next

    @staticmethod
    def run():
        def create_linked_list(arr):
            dummy = ListNode()
            current = dummy
            for val in arr:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        def print_linked_list(head):
            result = []
            while head:
                result.append(head.val)
                head = head.next
            print(result)

        list1 = create_linked_list([1, 2, 4])
        list2 = create_linked_list([1, 3, 4])

        solution = Solution()
        result = solution.mergeTwoLists(list1, list2)

        print_linked_list(result)


Solution.run()
