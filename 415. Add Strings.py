class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = ''

        a = list(num1)
        b = list(num2)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %10)
            carry //= 10

        return result[::-1]