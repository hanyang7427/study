# define binary tree node
class TreeNode:
    def __init__(self, data, left, right):
        self._data = data
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, treeNode):
        self._root = treeNode

    def insert(self, treeNode):
        # build a complete binary tree
        tList = []
        def insert_node(tree_node, p, treeNode):
            if tree_node._left is None:
                tree_node._left = treeNode
                #print("left:",treeNode._data)
                tList.append(tree_node._left)
                return
            elif tree_node._right is None:
                tree_node._right = treeNode
                #print("right:",treeNode._data)
                tList.append(tree_node._right)
                return
            else:
                tList.append(tree_node._left)
                tList.append(tree_node._right)
                insert_node(tList[p+1], p+1, treeNode)

        tList.append(self._root)
        insert_node(self._root, 0, treeNode)

        # print the result
        print("insert result:")
        for node in tList:
            print(node._data)



def BFS(tree):
    tLst = []
    def traverse(node, p):
        if node._left is not None:
            tLst.append(node._left)
            #print("node._left", node._left._data)
        if node._right is not None:
            tLst.append(node._right)
            #print("node._right", node._right._data)
        if p > (len(tLst)-2):
            #print("return at ", p)
            return
        else:
            traverse(tLst[p+1], p+1)
    tLst.append(tree._root)
    traverse(tree._root, 0)

    # print the result
    #for node in tLst:
    #    print node._data

def DFS(tree):
    tLst = []
    tLst.append(tree._root)
    while len(tLst) > 0:
        node = tLst.pop()
        print(node._data)
        if node._right is not None:
            tLst.append(node._right)
        if node._left is not None:
            tLst.append(node._left)

if __name__ == '__main__':
    TList = [1, 3, 2, 5, 4, 6, 8, 7, 9, 12, 11, 14, 13]

    tree = BinaryTree()
    for (i, j) in enumerate(TList):
        node = TreeNode(j, None, None)
        if i == 0:
           tree.make_tree(node)
        else:
           tree.insert(node)
    #print("BFS results:")
    #BFS(tree)
    # print("DFS results:")
    #DFS(tree)