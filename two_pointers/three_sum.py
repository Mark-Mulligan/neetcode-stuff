from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        prev_num = None

        for i in range(len(sorted_nums)):
            if i > 0:
                prev_num = sorted_nums[i - 1]

            num_1 = sorted_nums[i]

            if num_1 == prev_num:
                continue

            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                num_2 = sorted_nums[l]
                num_3 = sorted_nums[r]
                total = num_1 + num_2 + num_3

                if total == 0:
                    result.append([num_1, num_2, num_3])

                    while sorted_nums[l] == num_2:
                        l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return result


solution = Solution()
answer = solution.threeSum([-2, 0, 0, 2, 2])
print(answer)
