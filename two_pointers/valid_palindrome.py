import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        l = 0
        r = len(cleaned_s) - 1

        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1

        return True


solution = Solution()
answer = solution.isPalindrome("race a car")
print(answer)
