class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x=0
        y=len(height)-1
        max=0
        while x<y:
            temp=min(height[x],height[y])
            area=temp*(y-x)
            max=max(max,area)
            if height[x]<height[y]:
                x+=1
            else:
                y-=1
        return max