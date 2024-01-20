from typing import Optional
from utils import ListNode, create_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}
        curr = head

        while curr:
            if curr.val in seen_nodes:
                if curr in seen_nodes[curr.val]:
                    return True
                else:
                    seen_nodes[curr.val].append(curr)
            else:
                seen_nodes[curr.val] = [curr]

            curr = curr.next

        return False


node1 = ListNode(1)

node3 = ListNode(3, None)
node2 = ListNode(2, node3)
node1.next = node2


solution = Solution()
result = solution.hasCycle(node1)
print(result)
