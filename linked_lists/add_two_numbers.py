from typing import Optional
from utils import ListNode, create_linked_list

list1 = create_linked_list([2, 4, 3])
list2 = create_linked_list([5, 6, 4])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = node = ListNode()

        while l1 or l2:
            total = remainder

            if l1:
                total += l1.val
            if l2:
                total += l2.val

            if total > 9:
                remainder = 1
                node.next = ListNode(total - 10)
            else:
                remainder = 0
                node.next = ListNode(total)

            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if remainder:
            node.next = ListNode(remainder)

        return dummy.next


solution = Solution().addTwoNumbers(list1, list2)

while solution:
    print(solution.val)
    solution = solution.next
