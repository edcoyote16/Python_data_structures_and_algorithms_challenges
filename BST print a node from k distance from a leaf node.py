from binarytree import Node
# class Node:
#
#     def __init__(self, key):
#         self.key = key
#         self.left = self.right = None

MAX_HEIGHT = 10000

def printKDistantfromLeaf(node, k):
    global MAX_HEIGHT
    path = [None] * MAX_HEIGHT
    visited = [False] * MAX_HEIGHT
    # printKDistance(node, k, path, visited, 0)
    print(root)
    results = []
    kDistantFromLeafUtil(node, path, visited, 0, k, results)
    return results

def kDistantFromLeafUtil(node, path, visited, pathLen, k, results):
    # Base case


    if (node == None):
        return

    # append this Node to the path array
    path[pathLen] = node.value
    visited[pathLen] = False
    pathLen += 1

    # it's a leaf, so print the ancestor at
    # distance k only if the ancestor is
    # not already printed
    if (node.left == None and node.right == None and
            pathLen - k - 1 >= 0 and
            visited[pathLen - k - 1] == False):
        #print(path[pathLen - k - 1], end=" ")
        results+=[path[pathLen - k - 1]]
        visited[pathLen - k - 1] = True
        return

    # If not leaf node, recur for left
    # and right subtrees
    kDistantFromLeafUtil(node.left, path,
                         visited, pathLen, k, results)
    kDistantFromLeafUtil(node.right, path,
                         visited, pathLen, k, results)
    return

root = Node(3)
root.left = Node(8)
root.right = Node(9)
root.right.right = Node(3)
root.left.left = Node(11)
root.left.right = Node(7)
root.left.right.left = Node(6)
root.left.right.right = Node(12)



print(printKDistantfromLeaf(root, 2))

expected = [1, 2]
