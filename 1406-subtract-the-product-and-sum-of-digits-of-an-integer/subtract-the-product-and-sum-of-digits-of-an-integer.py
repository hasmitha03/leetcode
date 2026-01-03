class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits = 0
        product_digits = 1

        for ch in str(n):
            d = int(ch)
            sum_digits += d
            product_digits *= d

        return product_digits - sum_digits