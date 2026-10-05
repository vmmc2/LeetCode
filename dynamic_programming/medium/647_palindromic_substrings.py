class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        n = len(s)

        # Count the number of palindromic substrings of odd length:
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                answer += 1
                left -= 1
                right += 1

        # Count the number of palindromic substrings of even length:
        for i in range(n):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                answer += 1
                left -= 1
                right += 1

        return answer