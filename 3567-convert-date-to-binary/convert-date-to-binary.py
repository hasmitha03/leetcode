class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        s = ""
        dates = date.split('-')
        length = len(dates)
        for i in range(length):
            inte = bin(int(dates[i]))[2:]
            s += str(inte)
            if i != length-1:
                s += '-'
        return s 