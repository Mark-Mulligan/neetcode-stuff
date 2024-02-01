from typing import List
from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_hash = Counter(tasks)
        heap = []
        heapq.heapify([])

        for task in task_hash:
            heapq.heappush(heap, (-task_hash[task], task))

        task_count = 0
        while True:
            current_sequence = 0

            while current_sequence <= n and len(task_hash) > 0:
                if len(heap) > 0:
                    task = heapq.heappop(heap)

                    if task_hash[task[1]] == 1:
                        del task_hash[task[1]]
                    else:
                        task_hash[task[1]] -= 1

                task_count += 1
                current_sequence += 1

            if len(task_hash) == 0:
                break

            heap = []
            for task in task_hash:
                heapq.heappush(heap, (-task_hash[task], task))

        return task_count


solution = Solution()
answer = solution.leastInterval(
    ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2)
print(answer)
