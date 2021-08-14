def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
# sort a list containing 0, 1 and 2
# three-way Partitioning
def sort012(array):
    low = mid = 0
    high = len(array) - 1

    while mid <= high:

        if array[mid] == 0:  # current element is 0
            mid = mid + 1
        elif array[mid] != 0:
            swap(array, low, mid)
            low = low + 1
            mid = mid + 1
    return array

array=[0,1,0,3,12]
print(sort012(array))