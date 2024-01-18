from typing import Optional
from utils import create_linked_list, ListNode

list1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
list2 = create_linked_list([9, 9, 9, 9])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        remainder = 0
        while l1 and l2:
            total = l1.val + l2.val + remainder

            if total > 9:
                remainder = 1
                node.next = ListNode(total - 10)
            else:
                remainder = 0
                node.next = ListNode(total)
            node = node.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + remainder
            if total > 9:
                remainder = 1
                node.next = ListNode(total - 10)
            else:
                remainder = 0
                node.next = ListNode(total)
            node = node.next
            l1 = l1.next

        while l2:
            total = l2.val + remainder
            if total > 9:
                remainder = 1
                node.next = ListNode(total - 10)
            else:
                remainder = 0
                node.next = ListNode(total)
            node = node.next
            l2 = l2.next

        if remainder:
            node.next = ListNode(remainder)

        return dummy.next


solution = Solution()
answer = solution.addTwoNumbers(list1, list2)

while answer:
    print(answer.val)
    answer = answer.next
