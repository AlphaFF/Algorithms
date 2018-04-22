# 列表表示树结构

myTree = ['a', ['b', [], []], ['c', [], []]]


def BinaryTree(r):
    return [r, [], []]


# 插入左子节点
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


# 插入右子节点
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


class BinaryTree:
    """
    使用节点和引用来表示树
    """

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


# if __name__ == '__main__':
# 	r = BinaryTree('a')
# 	print(r.getRootVal())
# 	print(r.getLeftChild())
# 	r.insertLeft('b')
# 	print(r.getLeftChild())
# 	print(r.getLeftChild().getRootVal())
# 	r.getLeftChild().setRootVal('haha')
# 	print(r.getLeftChild().getRootVal())

# 分析树
from stack import Stack
import operator


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    print(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


# if __name__ == '__main__':
#     pt = buildParseTree("( ( 10 + 5 ) * 3 )")
#     p = evaluate(pt)
#     print(p)

# 树的遍历
# 前序遍历
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# 后序遍历
def posorder(tree):
    if tree:
        posorder(tree.getLeftChild())
        posorder(tree.getRightChild())
        print(tree.getRootVal())


# 后序遍历
def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


# 恢复表达式的完全括号版本
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '{' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = printexp(tree.getRightChild()) + '}'
    return sVal


# 计算分析树
def posordereval(tree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = posordereval(tree.getLeftChild())
        res2 = posordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


# 二叉堆操作
class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0


