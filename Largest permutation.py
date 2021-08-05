def largestPermutation(k, arr):
    indeces={}
    # creates the dictionary to hold the indeces of values
    for i in range(0, len(arr)):
        indeces[arr[i]]=i

    i =0
    max_element=len(arr)

    #
    while k>0 and max_element >1:
        max_element_index=indeces[max_element]
        if max_element != arr[i]:

            # replaces the leftmost value with the highest value
            arr[i], arr[max_element_index]= arr[max_element_index], arr[i]

            # updates the leftmost vallue index with the highest value index
            indeces[arr[i]], indeces[arr[max_element_index]]= i, indeces[arr[i]]

            # decreases the number of times characters can be swap
            k -= 1
        # continues to the next highest value in decreasing order
        max_element -= 1
        # continues to check the next value in the original array
        i += 1

    return arr

k = 2
arr = [4, 2, 3, 5, 1]
largestPermutation(k, arr)















