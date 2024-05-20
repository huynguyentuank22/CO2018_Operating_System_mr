class Node:
    def __init__(self, page):
        self.page = page
        self.left = None
        self.right = None
        self.parent = None

class LRU_SplayTree:
    def __init__(self, capacity):
        self.root = None
        self.hit = 0
        self.miss = 0
        self.size = 0
        self.capacity = capacity

    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        y.parent = x.parent
        x.parent = y
        if x.right != None:
            x.right.parent = x
        if y.parent != None:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        self.root = y
    
    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        y.parent = x.parent
        x.parent = y
        if x.left != None:
            x.left.parent = x
        if y.parent != None:
            if y.parent.left == x:
                y.parent.left = y
            else:
                y.parent.right = y
        self.root = y
    
    def splay(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x.parent.left == x:
                    self.rotateRight(x.parent)
                else:
                    self.rotateLeft(x.parent)
            elif x.parent.left == x and x.parent.parent.left == x.parent:
                self.rotateRight(x.parent.parent)
                self.rotateRight(x.parent)
            elif x.parent.right == x and x.parent.parent.right == x.parent:
                self.rotateLeft(x.parent.parent)
                self.rotateLeft(x.parent)
            elif x.parent.left == x and x.parent.parent.right == x.parent:
                self.rotateRight(x.parent)
                self.rotateLeft(x.parent)
            else:
                self.rotateLeft(x.parent)
                self.rotateRight(x.parent)

    def insertRec(self, curr, parrent, p):
        if curr == None:
            p.parent = parrent
            return p
        if p.page >= curr.page:
            curr.right = self.insertRec(curr.right, curr, p)
        else:
            curr.left = self.insertRec(curr.left, curr, p)
        return curr
    
    def insert(self, page):
        p = Node(page)
        if self.root == None:
            self.root = p
            self.size = self.size + 1
            return
        self.root = self.insertRec(self.root, None, p)
        self.size = self.size + 1
        self.splay(p)

    def search(self, page):
        tmp = self.root
        while tmp:
            if page == tmp.page:
                return tmp
            elif page < tmp.page:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return None

    def getHeight(self, root):
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        return max(leftHeight, rightHeight) + 1

    def deleteDeepest(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            if root.parent:
                if root.parent.left == root:
                    root.parent.left = None
                else:
                    root.parent.right = None
            self.size = self.size - 1
            del root
            return

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight >= rightHeight:
            return self.deleteDeepest(root.left)
        else:
            return self.deleteDeepest(root.right)

    def traverse(self, root):
        if root == None:
            return
        self.traverse(root.left)
        print(root.page, end = " ")
        self.traverse(root.right)

    def accessPage(self, page):
        tmp = self.search(page)    
        if tmp != None:
            self.splay(tmp)
            self.hit = self.hit + 1
        else:
            self.miss = self.miss + 1
            if self.size < self.capacity:
                self.insert(page)
            else:
                self.deleteDeepest(self.root)
                self.insert(page)

    def LRU_Op(self, arr, n):
        for i in range(n):
            print("Access Page: ", arr[i])
            self.accessPage(arr[i])
            self.traverse(self.root)
            print()

    def hit_ratio(self):
        return self.hit / (self.hit + self.miss)
    
    def free_cache(self):
        if self.root == None:
            return
        self.free_cache(self.root.left)
        self.free_cache(self.root.right)
        del self.root
        self.size = self.size - 1

if __name__ == '__main__':
    capacity = 4
    arr = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    n = len(arr)
    lru = LRU_SplayTree(4)
    lru.LRU_Op(arr, n)
    print("Hit Ratio: ", lru.hit_ratio())