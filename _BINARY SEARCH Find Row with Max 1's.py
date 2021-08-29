def binarySearch(arr, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or (arr[mid - 1] == 0)) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return binarySearch(arr, mid + 1, high)
        else:
            return binarySearch(arr, low, mid - 1)
    return -1


def findRow(matrix):
    max_row_index = 0
    max_ = -1
    row = len(matrix)
    col = len(matrix[0])
    for a in range(row):
        index = binarySearch(matrix[a], 0, col - 1)
        if index != -1 and col - index > max_:
            max_ = col - index
            max_row_index = a

    return max_row_index


# ok for all test cases
# import unittest
#
#
# class Test(unittest.TestCase):
#     def test_findRow_test1(self):
#         actual = findRow([[0, 1, 1, 1],
#                           [0, 0, 1, 1],
#                           [1, 1, 1, 1],
#                           [0, 0, 0, 0]])
#         expected = 2
#         self.assertEqual(actual, expected)
#
#     def test_findRow_test2(self):
#         actual = findRow([[1, 1, 1],
#                           [0, 0, 0],
#                           [1, 1, 0],
#                           [1, 0, 0]])
#         expected = 0
#         self.assertEqual(actual, expected)
#
#     def test_findRow_test3(self):
#         actual = findRow([[0, 0, 0, 1, 1],
#                           [0, 0, 1, 1, 1],
#                           [0, 0, 0, 0, 0],
#                           [0, 1, 1, 1, 1],
#                           [0, 0, 0, 0, 1]])
#         expected = 3
#         self.assertEqual(actual, expected)
#
#
# unittest.main(verbosity=2)