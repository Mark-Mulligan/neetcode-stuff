from typing import Optional
from utils import ListNode, create_linked_list, print_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


if __name__ == '__main__':
    test_input = create_linked_list([1, 2, 3, 4, 5])
    head = Solution().reverseList(test_input)
    print_linked_list(head)
