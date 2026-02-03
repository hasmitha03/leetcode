class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def digits(x):
            while x != 0:
                x, rem = divmod(x, 10)
                yield rem
        sum_digits = sum(digits(x))
        return sum_digits if x % sum_digits == 0 else -1