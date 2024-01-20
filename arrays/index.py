from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            temp = []

            if i > 0:
                prev_temp = result[i - 1]
                for index, val in enumerate(prev_temp):
                    if index == 0:
                        temp.append(val)
                    else:
                        temp.append(val + prev_temp[index - 1])

            temp.append(1)
            result.append(temp)

        return result


solution = Solution()
answer = solution.generate(5)
print(answer)
