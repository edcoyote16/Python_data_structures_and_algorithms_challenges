from binarytree import Node


# class Node:
#
# 	def __init__(self, key):
# 		self.key = key
# 		self.left = None
# 		self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def findInorderSuccessor(root):
    while root.left is not None:
        root = root.left
    return root

def Delete(root, key):

    if root is None:
        return root
    if key < root.value:
        root.left = Delete(root.left, key)
    elif key > root.value:
        root.right = Delete(root.right, key)
    else:
        if root.left is None and root.right is None:
            root = None
            return root
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = findInorderSuccessor(root.right)
        root.value = temp.value
        root.right = Delete(root.right, temp.value)
    return root


root = None
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 5)
root = insert(root, 10)
root = insert(root, 8)
root = insert(root, 15)
root = insert(root, 11)
root = insert(root, 12)
#root = insert(root, 19)

print('Inorder traversal of the given tree')
inorder(root)
print(root)

print('Delete 5')
root = Delete(root, 5)
print('Inorder traversal of the modified tree')
inorder(root)
print(root)

# print ('Delete 30')
# root = Delete(root, 30)
# print ('Inorder traversal of the modified tree')
# inorder(root)
# print(root)
#
# print ('Delete 50')
# root = Delete(root, 50)
# print ('Inorder traversal of the modified tree')
# inorder(root)
# print(root)