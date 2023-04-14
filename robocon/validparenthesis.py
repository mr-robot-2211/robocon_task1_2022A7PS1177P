class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
        if len(s) !=0:
            return False
        else:
            return True
