class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0

        nums, sign, num = [], '+', 0
        def process(nums, sign, num):
            if sign == '-':
                nums.append(-num)
            elif sign == '+':
                nums.append(num)
            elif sign == '*':
                nums.append(nums.pop() * num)
            elif sign == '/':
                nums.append(int(nums.pop() / num))

        for c in s:
            if c.isdigit():  # digit
                num = num * 10 + int(c)
            elif c != ' ':   # sign
                process(nums, sign, num)
                sign, num = c, 0
        process(nums, sign, num)
        return sum(nums)