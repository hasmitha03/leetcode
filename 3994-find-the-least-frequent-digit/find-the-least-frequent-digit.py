class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        return int(min(set(str(n)), key=lambda d: (str(n).count(d), d)))