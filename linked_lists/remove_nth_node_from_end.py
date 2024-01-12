from typing import Optional
from utils import ListNode, create_linked_list, print_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


if __name__ == "__main__":
    linked_list = create_linked_list([1])
    head = Solution().removeNthFromEnd(linked_list, 1)
    print_linked_list(head)
