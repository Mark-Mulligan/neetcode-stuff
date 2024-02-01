from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, -num)

        i = 0
        result = 0
        while i < k:
            result = heapq.heappop(heap)
            i += 1

        return -result


solution = Solution()
answer = solution.findKthLargest([-1, -1], 2)
print(answer)
