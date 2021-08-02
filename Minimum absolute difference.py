from itertools import combinations
my_result=1000000000000
arrays=input().split()
my_numbers=combinations(arrays, 2)
my_numbers=list(my_numbers)
for a in my_numbers:
    if abs(a[0]-a[1])<my_result:
        my_result=abs(a[0]-a[1])

print(my_result)


def minimumAbsoluteDifference(arr):
    return min(arr[i+1]-arr[i] for i in range(len(arr)-1))
input()
arr = sorted(map(int,input().split()))
print(minimumAbsoluteDifference(arr))