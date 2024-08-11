class Solution:
    def myPow(self, x: float, n: int) -> float:
        invert = True if n < 0 else False

        def fastExp(x, n):
            if n == 0:
                return 1
            temp = fastExp(x, n // 2)
            value = temp * temp
            if n % 2 == 1:
                value *= x
            
            return value

        value = fastExp(x, abs(n))

        if invert:
            return 1/value

        return value
