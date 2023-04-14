from math import factorial
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(numRows):
            cols=[]
            for j in range(i+1):
                cols.append(factorial(i)/(factorial(j)*factorial(i-j)))
            arr.append(cols)
        return arr
     