#Maximum squared distance
#Four integers A, B, C, D are given. The integers can be used to describe two points on a plane by assigning their values to the coordinates of the points. Each integer has to be assigned to exactly one coordinate. Your task is to assign the integers A, B, C and D to the coordinates of two points in such a way as to maximize the squared distance between those points.
#
#int getMaxDistanceSquare(int A, int B, int C, int D)
#
#Assume that:
#
#A, B, C and D are integers within the range [-5000, 5000]
#
#For example, let's consider the following values:
#A = 1
#B = 1
#C = 2
#D = 3
#
#We have:
#(1, 1) <=> (2, 3)  or (3, 2) squared distance = 5 or 5      MAX = 5
#(1, 2) <=> (1, 3)      (3, 1)                                1     5
#(1, 3) <=> (1, 2)      (2, 1)                                1     5
#
#For Example,
#
#A = 2
#B = 4
#C = 2
#D = 4
#
#We have:
#(2, 4) <=> (2, 4) or (4, 2) squared distance = 0 or 8      MAX = 8
#(2, 2) <=> (4, 4)                                              8
#(2, 4) <=> (4, 2) or (2, 4)                                8     0
#
#For Example,
#A = 1
#B = 2
#C = 3
#D = 4
#
#We have:
#(1, 2) <=> (3, 4) or (4, 3) squared distance = 8 or 10    MAX = 10
#(1, 3) <=> (2, 4) or (4, 2)                                1     10
#(1, 4) <=> (2, 3) or (3, 2)                                1      8
#

# Solution in Python

def max_dist(a,b,c,d):
    nums = [a,b,c,d]
    nums.sort()
    return (nums[3]-nums[0])**2 +  (nums[2]-nums[1])**2
