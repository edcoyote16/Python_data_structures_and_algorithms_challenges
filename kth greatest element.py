from binarytree import tree, bst, heap, Node
# class Node:
#
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

#ok for all test cases required
def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.value:
        root.left = insert(root.left, key)

    else:
        root.right = insert(root.right, key)

    return root


def kthLargest(root, i, k):
    if root == None:
        return -1, i
    val, i = kthLargest(root.right, i, k)
    if val != -1:   return val, i
    i += 1
    if(i == k):
        return root.value, i
    return kthLargest(root.left, i, k)

def findKthLargest(root, k):
    i = 0
    return kthLargest(root, i, k)

root = None
keys = [22,14,25,13,23,32,28,40,26]
#keys = [50,1,3,4,5,6,7,67,8,9,10,99,200,2,13,12,49,38]
for key in keys:
    root = insert(root, key)
print(root)
print(findKthLargest(root, 8))