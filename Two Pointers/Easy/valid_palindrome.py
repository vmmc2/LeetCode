class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        s = list(filter(lambda ch: ch.isalnum(), s))

        left = 0
        right = len(s) - 1

        while(left < right):
            if(s[left] != s[right]):
                return False
            left += 1
            right -= 1

        return True
