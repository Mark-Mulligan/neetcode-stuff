from typing import List
from collections import Counter
from copy import deepcopy

# Brute Force


class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s_candidates = sorted(candidates)
        queue = []
        combinations = []

        for num in s_candidates:
            if num < target:
                queue.append({'sum': num, 'list': [num]})
            elif num == target:
                combinations.append([num])
            else:
                break

        queue_hashes = []
        while len(queue) > 0:
            queue_item = queue.pop()

            for num in s_candidates:
                queue_item_copy = deepcopy(queue_item)
                queue_item_copy['sum'] += num
                queue_item_copy['list'].append(num)
                print(queue_hashes)

                hash = Counter(queue_item_copy['list'])
                if hash in queue_hashes:
                    continue
                elif queue_item_copy['sum'] < target:
                    queue.append(queue_item_copy)
                    queue_hashes.append(hash)
                elif queue_item_copy['sum'] == target:
                    queue_hashes.append(hash)
                    combinations.append(queue_item_copy['list'])
                else:
                    break

        return combinations

        pass


class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candiates = sorted(candidates)
        combinations = []
        queue = []

        for num in sorted_candiates:
            if num < target:
                queue.append({num: 1})
            elif num == target:
                combinations.append({num: 1})
            else:
                break

        while len(queue) > 0:
            queue_item = queue.pop()

            for num in sorted_candiates:
                current_sum = 0

                for key in queue_item:
                    current_sum += int(key) * queue_item[key]

                current_sum += num
                queue_item_copy = queue_item.copy()
                if current_sum < target:
                    if num in queue_item_copy:
                        queue_item_copy[num] += 1
                    else:
                        queue_item_copy[num] = 1
                    queue.append(queue_item_copy)
                elif current_sum == target:
                    if num in queue_item_copy:
                        queue_item_copy[num] += 1
                    else:
                        queue_item_copy[num] = 1

                    if queue_item_copy not in combinations:
                        combinations.append(queue_item_copy)
                else:
                    break

        result = []
        for combo_hash in combinations:
            temp = []
            for key in combo_hash:
                if combo_hash[key] == 1:
                    temp.append(key)
                else:
                    for i in range(int(combo_hash[key])):
                        temp.append(key)

            result.append(temp)

        return result


solution = Solution2()
answer = solution.combinationSum([8, 2, 3, 5], 8)
print(answer)
