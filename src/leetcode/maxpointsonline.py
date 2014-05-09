'''
Created on May 7, 2014

http://oj.leetcode.com/problems/max-points-on-a-line/

@author: vsa
'''
# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        max = 0
        lines = {}
        for point1 in points:
            p1 = point1.x
            q1 = point1.y
            for point2 in points:
                p2 = point2.x
                q2 = point2.y
                if p1 != p2 or q1 != q2:
                    if p2 == p1:
                        a = float("inf")
                    else:
                        a = (q2 - q1) / (p2 - p1)
                    b = q1 - p1 * (a)

                    line = (a, b)
                    if line in lines:
                        count = lines[line]
                        lines[line] = count + 1
                        if max < count + 1:
                            max = count + 1
                    else:
                        lines[line] = 1
                        if max == 0:
                            max = 1
        return max

if __name__ == '__main__':
    p0 = Point()
    p1 = Point(1,1)
    p2 = Point(2,2)
    p3 = Point(3,3)
    points = set()
    points.add(p0)
    points.add(p1)
    points.add(p2)
    points.add(p3)

    solution = Solution()
    max = solution.maxPoints(points)
    print(max)
    pass
