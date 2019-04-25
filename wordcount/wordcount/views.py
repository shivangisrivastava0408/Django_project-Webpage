from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def bst(request):
    text=request.GET["list"]
    l1=list(map(int,text.split()))
    t=Node(l1[0])
    #g=t.levelOrder(t)
    for w in range(1,len(l1)):
        t.insert(l1[w])
    return render(request,'bst.html',{'initial':text,'pre':t.PreorderTraversal(t),'in':t.InorderTraversal(t),'post':t.PostorderTraversal(t),'sum':plus(t.levelOrder(t))})

def sort(request):
    data=request.GET["list"]
    l=list(map(int,data.split()))
    insertionSort(l)
    return render(request,'sort.html',{'sortedlist':data,'final':l})


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def plus(d):
    ans=[]
    for w in range(len(d)):
        ans.append(sum(d[w]))
    return(ans)

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.InorderTraversal(root.left)
            res.append(root.data)
            res = res + self.InorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def levelOrder(self, root):
        if root == None:
            return []

        res = []
        nodes = [root]
        while nodes:
            res.append([node.data for node in nodes])
            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes

        return res