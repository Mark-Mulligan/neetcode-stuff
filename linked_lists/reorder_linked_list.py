from typing import Optional
from utils import ListNode, create_linked_list, print_linked_list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_refs_list = []
        curr = head
        while curr:
            node_refs_list.append(curr)
            curr = curr.next

        index = 0
        while index < len(node_refs_list):
            if index % 2 == 0:
                current_node = node_refs_list[index // 2]

                if index == len(node_refs_list) - 1:
                    current_node.next = None
                else:
                    current_node.next = node_refs_list[len(
                        node_refs_list) - 1 - (index // 2)]
            else:
                current_node = node_refs_list[len(
                    node_refs_list) - 1 - (index // 2)]

                if index == len(node_refs_list) - 1:
                    current_node.next = None
                else:
                    current_node.next = node_refs_list[(index // 2) + 1]

            index += 1


if __name__ == "__main__":
    linked_list = create_linked_list([1, 2, 3, 4, 5])
    Solution().reorderList(linked_list)
    print_linked_list(linked_list)
