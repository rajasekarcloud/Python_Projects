# Challenge: Distance Between Two 3D Points
# Write a Python program that calculates the distance between two 3D points.
# [1,2,3] and [1,2,3] = 0
# [3,4,5] and [1,3,5] = 2.23607
import math;
pointA=[3,4,5];
pointB=[1,3,5];
sum=0;
for i in range(len(pointA)):
    sum += (pointB[i] - pointA[i])**2;
print(f'{math.sqrt(sum)}');
