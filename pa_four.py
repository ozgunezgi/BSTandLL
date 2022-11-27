class BSTNode:
    # Class for Binary Search Tree Node
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LinkedListNode:
    # Class for LinkedList Node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def inorder(root):
    if root is None:
        return []
    left = inorder(root.left)
    right = inorder(root.right)
    return left + [root.data] + right


def BST2LinkedList(root):
    L = inorder(root)
    pointer = None

    for i in L:
        if pointer is None:
            pointer = LinkedListNode(i)
        else:
            current = pointer
            while current.next != None:
                current = current.next
            current.next = LinkedListNode(i)

    return pointer


def mergeBSTs(root1, root2):
    l1 = inorder(root1)
    l2 = inorder(root2)

    l3 = l1 + l2
    l3.sort()

    root3 = None

    for i in l3:
        if root3 is None:
            root3 = BSTNode(i)
            current = root3

        else:
            current.right = BSTNode(i)
            current = current.right

    return root3


def printLinkedList(llist):
    # Takes the output of BST2LinkedList and prints its contents
    current = llist
    while current.next != None:
        print(str(current.data) + " -> ", end="")
        current = current.next
    print(current.data)


def printBST(bst_root):
    if bst_root is None:
        return

    printBST(bst_root.left)
    print(bst_root.data)
    printBST(bst_root.right)


"""
TASK 1

root = BSTNode(20)
root.left = BSTNode(10)
root.right = BSTNode(30)
root.right.left = BSTNode(25)
root.right.right = BSTNode(100)


printBST(root)
llist = BST2LinkedList(root)
printLinkedList(llist)

TASK 2

root1 = BSTNode(20)
root1.left = BSTNode(10)
root1.right = BSTNode(30)
root1.right.left = BSTNode(25)
root1.right.right = BSTNode(100)

root2 = BSTNode(50)
root2.left = BSTNode(5)
root2.right = BSTNode(70)

root3 = mergeBSTs(root1, root2)
printBST(root3)

"""
