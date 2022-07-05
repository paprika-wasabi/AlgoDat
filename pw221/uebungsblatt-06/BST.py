"""
Class representing a binary search tree with minimal funcitonality
Copyright 2020, University of Freiburg
Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""


class TreeElement:
    '''
        represents a node in binary tree
        Attributes:
            key - the value according to which a binary search tree is sorted
            parent - TreeElement representing the parent in the tree
            left - TreeElement representing the left child in the tree
            right - TreeElement representing the right child in the tree
    '''

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BST:
    '''
        class that represents a binary search tree
        Attributes:
            root - a TreeElement that represents the root of the tree
    '''

    def __init__(self, root=None):
        self.root = root

    def insert(self, x):
        '''
            inserts a given key into the binary search tree
            Parameters:
                x - comparable key to insert
        '''
        if self.root is None:
            self.root = TreeElement(x)
            return None
        else:
            currentnode = self.root
            while currentnode is not None:
                # if currNode is emty leaf then leaf is x.
                if x < currentnode.key:
                    if currentnode.left is None:
                        currentnode.left = TreeElement(x, currentnode)
                        return None
                    # else move to next left leaf.
                    else:
                        currentnode = currentnode.left
                else:
                    # if currNode is emty leaf then leaf is x.
                    if x > currentnode.key:
                        if currentnode.right is None:
                            currentnode.right = TreeElement(x, currentnode)
                            return None
                        # else move to next right leaf.
                        else:
                            currentnode = currentnode.right
        return None

    def getrange(self, xmin, xmax):
        '''
            returns all keys x with xmin <= x < xmax.

            Implementation hints: May use either additional
            parameters or call a recursive subfunction with
            additional parameters.

            Parameters:
                xmin - lower bound (including)
                xmax - upper bound (excluding)

            Returns:
                List of keys with xmin <= x < xmax

            Unit tests:
                >>> bst = BST()
                >>> bst.insert(3); bst.insert(1); bst.insert(6)
                >>> bst.insert(2); bst.insert(5); bst.insert(4)
                >>> sorted(bst.getrange(2, 5))
                [2, 3, 4]
        '''
        retarray = []
        # "starting getRangeFunction"

        def traverse(node):
            if node is None:
                return retarray
            if xmin <= node.key < xmax:
                retarray.append(node.key)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return retarray

    def insert_from_file(self, filename='input.txt'):
        '''
            opens a file and inserts the content into the tree
            Parameters:
                filename - filename of file, must be in same filder
        '''

        with open(filename) as input:
            words = input.read().splitlines()
            for word in words:
                print("inserting :" + word)
                self.insert(word)


# manuel test
# bst = BST()
# print(bst.insert(3))
# bst.insert(1)
# bst.insert(6)
# bst.insert(2)
# bst.insert(5)
# bst.insert(4)

# print("finish insertion")
# print(sorted(bst.getrange(2, 5)))
# print('done')

# try
# bst2 = BST()
# print('starting insertion string from input.txt')
# bst2.insert_from_file("/Users/paramiewillmann/Desktop/AlgoDat/pw221/uebungsblatt-06/input.txt")
# print('insertion finish')
