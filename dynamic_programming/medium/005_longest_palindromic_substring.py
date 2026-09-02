class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome_length = 0
        max_palindrome = ""
        
        for i in range(len(s)):
            # Dealing with odd length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_palindrome_length:
                    max_palindrome_length = right - left + 1
                    max_palindrome = s[left : right + 1]
                left -= 1
                right += 1
                
            # Dealing with even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_palindrome_length:
                    max_palindrome_length = right - left + 1
                    max_palindrome = s[left : right + 1]
                left -= 1
                right += 1

        return max_palindrome