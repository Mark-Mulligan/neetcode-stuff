from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone_1 = abs(heapq.heappop(heap))
            stone_2 = abs(heapq.heappop(heap))

            if stone_1 == stone_2:
                continue
            else:
                result = stone_1 - stone_2
                heapq.heappush(heap, -result)

        if len(heap):
            return abs(heap[0])

        return 0


solution = Solution()
answer = solution.lastStoneWeight([2, 7, 4, 1, 8, 1])
print(answer)
