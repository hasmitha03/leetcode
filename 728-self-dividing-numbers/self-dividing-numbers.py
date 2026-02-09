class Solution(object):
    def selfDividingNumbers(self, left, right):
        lst=[]
        for num in range(left,right+1):
            res,temp=True,num
            while num>0:
                digit=num%10
                if digit==0:
                    res=False
                    break
                elif temp%digit!=0:
                    res=False
                    break                                                                       
                else:
                    num//=10        
            if res:
                lst.append(temp)
        return lst