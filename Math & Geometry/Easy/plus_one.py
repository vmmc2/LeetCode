class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        n = len(digits)
        carry = 0
        idx = 0

        while idx < n:
            if idx == 0:
                result = digits[idx] + 1
                digits[idx] = result % 10
                carry = result // 10
            else:
                result = digits[idx] + carry
                digits[idx] = result % 10
                carry = result // 10
            idx += 1

        if carry == 1:
            digits.append(carry)

        digits.reverse()

        return digits
