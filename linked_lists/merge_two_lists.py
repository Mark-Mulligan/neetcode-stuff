from typing import Optional
from utils import ListNode, create_linked_list, print_linked_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2
        return dummy.next


if __name__ == '__main__':
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([2, 4, 5])
    head = Solution().mergeTwoLists(list1, list2)
    print_linked_list(head)
