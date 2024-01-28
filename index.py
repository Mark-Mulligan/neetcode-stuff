from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0

        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] != 0:
                p1 += 1
                p2 += 1
                continue

            if nums[p2] == 0:
                p2 += 1
                continue

            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp

        print(nums)


solution = Solution()
# [0,1,0,3,12]
# [0, 0, 1]
answer = solution.moveZeroes([1, 0, 1, 0, 3, 12])
