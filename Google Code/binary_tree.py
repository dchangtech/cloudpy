# myTree = ['a',   #root
#       ['b',  #left subtree
#        ['d', [], []],
#        ['e', [], []] ],
#       ['c',  #right subtree
#        ['f', [], []],
#        [] ]
#      ]

# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])


def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1) # If no index is specified, a.pop() removes and returns the last item in the list
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
print('whole tree r',r) 
l = getLeftChild(r)
print('left sub-stree',l) # left sub-stree

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))



quiz = BinaryTree('a')
insertLeft(quiz,'b')
insertRight(quiz,'c')
insertRight(getRightChild(quiz),'f')
insertLeft(getRightChild(quiz),'e')
insertRight(getLeftChild(quiz),'d')
print('quiz tree',quiz)