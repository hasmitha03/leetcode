class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        od_sum = 0
        e_sum = 0
        n = list(str(n))
        l = len(n)
        for i in range(1,l+1):
            if i %2 != 0:
                od_sum += int(n[i-1])
            else:
                e_sum += int(n[i-1])
        return od_sum - e_sum