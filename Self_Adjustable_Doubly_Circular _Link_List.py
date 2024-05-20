class Node:
    def __init__(self, page):
        self.page = page
        self.next = None
        self.prev = None

class LRU_LinkList:
    def __init__ (self, capacity):
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.hit = 0
        self.miss = 0

    
    def insertToFront(self, page):
        if self.head == None:
            self.head = self.tail = Node(page)
        else:
            new_node = Node(page)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size = self.size + 1
    
    def deleteAt(self, index):
        if index == 0:
            tmp = self.head
            page = tmp.page
            self.head = tmp.next
            if self.head != None:
                self.head.prev = None
            else:
                self.head = self.tail = None
                del tmp
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            page = curr.next.page
            tmp = curr.next
            if curr.next.next != None:
                tmp.next.prev = curr
                curr.next = tmp.next
                del tmp
            else:
                curr.next = None
                self.tail = curr
                del tmp
        self.size = self.size - 1
        return page
    
    def deleteAtLast(self):
        page = self.deleteAt(self.size - 1)
        return page

    def moveToFront(self, index):
        if self.head == None:
            return
        page = self.deleteAt(index)
        self.insertToFront(page)

    def searchPage(self, page):
        if self.head == None:
            return -1
        tmp = self.head
        index = 0
        while True:
            if tmp.page == page:
                return index
            if tmp == self.tail:
                return -1
            tmp = tmp.next
            index = index + 1

    def traverse(self):
        if self.head == None:
            return
        tmp = self.head
        print("head -> ", end = "")
        while True:
            print(tmp.page, end = " -> ")
            if tmp == self.tail:
                break
            tmp = tmp.next
        print("tail")

    def accessPage(self, page):
        index = self.searchPage(page)
        if index != -1:  
            self.hit = self.hit + 1
            self.moveToFront(index)
        else:
            self.miss = self.miss + 1
            if self.size < self.capacity:
                self.insertToFront(page)
            else:
                self.deleteAtLast()
                self.insertToFront(page)

    def LRU_Op(self, arr, n):
        for i in range(n):
            # print("Access Page: ", arr[i])
            self.accessPage(arr[i])
            self.traverse()

    def hit_ratio(self):
        return self.hit / (self.hit + self.miss)
    
    def free_cache(self):
        while (self.size):
            self.deleteAt(0)

if __name__ == '__main__':
    capacity = 5
    lru = LRU_LinkList(capacity)
    arr = [1, 2, 3, 4, 5, 2, 10, 7, 11, 1]
    n = len(arr)
    lru.LRU_Op(arr, n)
    print("Hit Ratio: ", lru.hit_ratio())
    