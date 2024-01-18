from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        index = 0
        n1_copy = nums1.copy()
        n2_copy = nums2.copy()

        while p1 < m and p2 < n:
            print(p1, p2, n1_copy[p1], n2_copy[p2])
            if n1_copy[p1] < n2_copy[p2]:
                print('this ran')
                nums1[index] = n1_copy[p1]
                p1 += 1
            else:
                nums1[index] = n2_copy[p2]
                p2 += 1
            index += 1

        while p1 < m:
            nums1[index] = n1_copy[p1]
            p1 += 1
            index += 1

        while p2 < n:
            nums1[index] = n2_copy[p2]
            p2 += 1
            index += 1


list1 = [1, 2, 3, 0, 0, 0]
list2 = [2, 5, 6]

solution = Solution()
solution.merge(list1, 3, list2, 3)
print(list1)
