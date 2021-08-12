def findMaxValue(array, start, end):
    # Only one element is present in array[start..end]
    if start == end:
        return array[start]
        # If there are two elements and first is greater then the first element is maximum */
    if end == start + 1:
        if array[start] >= array[end]:
            return array[start];
        else:
            # If there are two elements and second is greater then the second element is maximum
            return array[end]
    mid = (start + end) // 2  # low + (high - low)/2
    # If we reach a point where arr[mid] is greater than both of its adjacent elements
    # array[mid-1] and array[mid+1], then array[mid] is the maximum element
    if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
        return array[mid]
        # If array[mid] is greater than the next element and smaller than the previous element
        # then maximum lies on left side of mid */
    if array[mid] > array[mid + 1] and array[mid] < array[mid - 1]:
        return findMaxValue(array, start, mid - 1)
    else:  # when array[mid] is greater than array[mid-1] and smaller than array[mid+1]
        return findMaxValue(array, mid + 1, end)

print(findMaxValue([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1],0,10))