# 树的类定义
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newNode):
        if not self.leftChild:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = BinaryTree

    def insert_right(self, newNode):
        if not self.rightChild:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, Obj):
        self.key = Obj

    def get_root_val(self):
        return self.key


# 栈的类定义, 后进先出
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# 分析树
def buildParseTree(fpexp):
    fp_list = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+' , '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+' , '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError

    return e_tree


# 评估分析树
def evaluate(parseTree):
    import operator
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_c = parseTree.get_left_child()
    right_c = parseTree.get_right_child()
    if left_c and right_c:
        fn = opers[parseTree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parseTree.get_root_val()


pt = buildParseTree("( ( ( 10 + 5 ) * 3 ) + ( 4 * 10 ) )")
print(evaluate(pt))


prev, res = [root], []
while prev:
    curr = []
    val = sum([node.val for node in prev]) / len(prev)
    res.append(val)
    while prev:
        node = prev.pop()
        if node.left:
            curr.append(node.left)
        if node.right:
            curr.append(node.right)
    prev = curr
return res

