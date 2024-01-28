from typing import Optional
from utils import ListNode, create_linked_list


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen_values = {}
        curr = head
        prev = None
        while curr:
            if curr.val in seen_values:

                while curr and curr.val in seen_values:
                    curr = curr.next

                prev.next = curr

                if curr:
                    seen_values[curr.val] = 1
                else:
                    break
            else:
                seen_values[curr.val] = 1

            prev = curr
            curr = curr.next

        return head


list1 = create_linked_list([1, 1, 2, 3, 3, 5, 5, 5, 5, 5])


solution = Solution()
result = solution.deleteDuplicates(list1)

while result:
    print(result.val)
    result = result.next
