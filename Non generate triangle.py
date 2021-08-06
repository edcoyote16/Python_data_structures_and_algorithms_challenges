n=6
A=[1, 1, 1, 2, 3, 5]

# n = int(input())
# A = sorted(int(i) for i in input().split())

i = n-3
# This loop traverse from right to left, starting at the index -3 because it is
# checking the sequence of three numbers such that a + b > c and b + c > a and
# a + c > b
while i >= 0 and (A[i] + A[i+1] <= A[i+2]) :
    # then goes to the left one
    i -= 1
# when the condition is met, then it checks the index is at least 0
if i >= 0 :
    # and then it prints it
    print(A[i],A[i+1],A[i+2])
else :
    # otherwise it prints -1
    print(-1)