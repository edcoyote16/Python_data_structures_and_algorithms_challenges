def largestPermutation(k, arr):
    indeces={}
    for i in range(0, len(arr)):
        indeces[arr[i]]=i

    i =0
    max_element=len(arr)

    while k>0 and max_element >1:
        max_element_index=indeces[max_element]
        if max_element != arr[i]:
            arr[i], arr[max_element_index]= arr[max_element_index], arr[i]
            indeces[arr[i]], indeces[arr[max_element_index]]= i, indeces[arr[i]]
            k -= 1
        max_element -= 1
        i += 1

    return arr

k = 1
arr = [4, 2, 3, 5, 1]
largestPermutation(k, arr)















