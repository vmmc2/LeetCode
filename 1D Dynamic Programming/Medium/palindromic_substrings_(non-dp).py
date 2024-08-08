class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0
        n = len(s)

        for i in range(0, n):
            # Checking odd length palindrome
            answer += 1

            mid = i
            left, right = mid - 1, mid + 1

            while left >= 0 and right <= n - 1:
                if s[left] == s[right]:
                    answer += 1
                    left -= 1
                    right += 1
                else:
                    break

            # Checking even length palindrome
            left, right = i, i + 1

            while left >= 0 and right <= n - 1:
                if s[left] == s[right]:
                    answer += 1
                    left -= 1
                    right += 1
                else:
                    break

        return answer
