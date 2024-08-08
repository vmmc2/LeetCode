class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        answer, lenAnswer = s[0], 1

        for i in range(0, n):
            # Considering an odd length palindrome
            middle = i
            left, right = middle - 1, middle + 1
            while left >= 0 and right <= n - 1:
                if s[left] == s[right]:
                    if len(s[left:right+1]) > lenAnswer:
                        answer, lenAnswer = s[left:right+1], len(s[left:right+1])
                    left -= 1
                    right += 1
                else:
                    break

            # Considering an even length palindrome
            left = i
            right = i + 1

            while left >= 0 and right <= n - 1:
                if s[left] == s[right]:
                    if len(s[left:right+1]) > lenAnswer:
                        answer, lenAnswer = s[left:right+1], len(s[left:right+1])
                    left -= 1
                    right += 1
                else:
                    break

        return answer
