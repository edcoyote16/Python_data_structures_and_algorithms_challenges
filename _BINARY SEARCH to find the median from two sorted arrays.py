def find(first, second, start_f, start_s, end_f, end_s):
    # 1 element in each  array  # median of sorted array made of two arrays will be
    if (end_f - start_f == 1):
    # sum of both elements by 2
        return (max(first[start_f], second[start_s]) + min(first[end_f], second[end_s])) / 2
    # calculating medians
    m1 = median(first, start_f, end_f)
    m2 = median(second, start_s, end_s)
    if (m1 == m2):
        return m1
    # if m1 < m2 then median must exist in array1[m1....] and array2[....m2]#
    elif (m1 < m2):
        return find(first, second, (end_f + start_f + 1) // 2, start_s, end_f, (end_s + start_s + 1) // 2)
    # if m1 > m2 then median must exist in array1[....m1] and array2[m2...] #
    else:
        return find(first, second, start_f, (end_s + start_s + 1) // 2, (end_f + start_f + 1) // 2, end_s)

def median(array, start, end):
    n = end - start + 1
    if (n % 2 == 0):
        return (array[start + int(n // 2)] + array[start + (int(n // 2) - 1)]) // 2
    else:
        return array[start + int(n // 2)]

#if __name__ == "__main__":

first = [1, 3, 5, 7, 9]
second = [2, 4, 6, 8, 10]

n1 = len(first)
n2 = len(second)

if (n1 != n2):
    print("size not equal")
elif (n1 == 0):\
    print("Arrays are empty.")
elif (n1 == 1):\
    print((first[0] + second[0]) // 2)
else:
    print("Median is " , find(first, second, 0, 0,len(first) - 1, len(second) - 1))