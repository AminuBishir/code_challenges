'''
Title: Adding solution for hour glass challegen
From: HackerRank -https://www.hackerrank.com/challenges/2d-array/problem

Description:

Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in  to be a subset of values with indices falling
in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in , and an hourglass sum is the sum of an
hourglass' values. Calculate the hourglass sum for every hourglass in ,
then print the maximum hourglass sum.

INPUT: a 2D 6x6 array of integers
OUTPUT: The sum of numbers in a hour glass having the highest sum

'''

# Complete the hourglassSum function below.
def hourglassSum(arr):

	#initial top element in the hour glass
	t1=arr[0][0]
	t2=arr[0][1]
	t3=arr[0][2]

	#initial middle element in the hour glass
	m = arr[1][1]

	#initial bottom elements in the hour glass
	b1=arr[2][0]
	b2=arr[2][1]
	b3=arr[2][2]

	#to hodl the highest sum of the hour glass
	high_sum = t1+t2+t3+m+b1+b2+b3

	#loop though the array/list column wise
	for i in range(4):
		#loop through the array/list row wise
		for j in range(4):
			#middle element in the hour glass
			t1=arr[i][j]
			t2=arr[i][j+1]
			t3=arr[i][j+2]

			#middle element in the hour glass
			m = arr[i+1][j+1]

			#bottom elements in the hour glass
			b1=arr[i+2][j]
			b2=arr[i+2][j+1]
			b3=arr[i+2][j+2]
			
			hour_glass = t1+t2+t3+m+b1+b2+b3
			print(hour_glass)
			if(hour_glass > high_sum):
				high_sum = hour_glass
	return high_sum