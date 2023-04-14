class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u=0
        l=0    
        for i in moves:
            if (i=="U"):
                u+=1
            elif(i=="D"):
                u-=1
            elif(i=="L"):
                l+=1
            elif(i=="R"):
                l-=1
        if (l==0 and u==0):
            return True
        return False