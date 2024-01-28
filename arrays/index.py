from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        is_odd = False

        if total_length % 2 != 0:
            is_odd = True
            median_target = math.ceil(total_length / 2)

        p1 = 0
        p2 = 0

        while p1 + p2 < median_target:
            pass

        if nums1[p1] < nums2[p2]:
            p1 += 1
        else:
            p2 += 1

        pass


solution = Solution()
answer = solution.findMedianSortedArrays([1, 2], [3, 4])
print(answer)
