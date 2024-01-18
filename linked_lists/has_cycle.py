from typing import Optional
from utils import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}

        curr = head
        while curr:
            if seen_nodes.get(curr.val, None):
                if curr in seen_nodes[curr.val]:
                    return True
                else:
                    seen_nodes[curr.val].append(curr)
            else:
                seen_nodes[curr.val] = [curr]
            curr = curr.next

        return False
