class Node:
    def __init__(self, page, freq = 1):
        self.page = page
        self.freq = freq
        self.prev = None
        self.next = None

    def increment_freq(self):
        # print('Incrementing frequency')
        self.freq = self.freq + 1

class Level:
    def __init__(self, freq):
        self.top = None
        self.bot = None
        self.freq = freq
        self.next = None
        self.size = 0

    def insertToFront(self, page, freq = 1):
        if self.next == None:
            self.next = Node(page, freq)
        else:
            newNode = Node(page, freq)
            newNode.next = self.next
            newNode.prev = self
            self.next.prev = newNode
            self.next = newNode
        self.size = self.size + 1
    
    def deleteAt(self, index):
        if self.next == None:
            return (None, None)
        if index == 0:
            tmp = self.next
            page = tmp.page
            freq = tmp.freq
            self.next = tmp.next
            if self.next != None:
                self.next.prev = self
            else:
                self.next = None
                del tmp
        else:
            curr = self.next
            for _ in range(index-1):
                curr = curr.next
            page = curr.next.page
            freq = curr.next.freq
            tmp = curr.next
            if curr.next.next != None:
                tmp.next.prev = curr
                curr.next = tmp.next
                del tmp
            else:
                curr.next = None
                del tmp
        self.size = self.size - 1
        return (page, freq)

    def moveToFront(self, index):
        if self.next == None:
            return
        page, freq = self.deleteAt(index)
        self.insertToFront(page, freq)

class LRU_SkipList:
    def __init__(self, capacity, max_freq):
        self.head = self.tail = None
        self.capacity = capacity
        self.size = 0
        self.hit = 0
        self.miss = 0
        self.max_freq = max_freq

    def insertToFrontOfBottomLayer(self, page):
        if self.head == None:
            self.head = self.tail = Level(self.max_freq)
        self.head.insertToFront(page)
        self.size = self.size + 1

    def deleteAtLastOfBottomLayer(self):
        self.head.deleteAt(self.head.size - 1)
        self.size = self.size - 1
    
    def searchPage(self, page):
        if self.head == None:
            return (None, None, None)
        level = self.tail
        while level != None:
            if level.next == None:
                level = level.bot
            else:
                curr = level.next
                index = 0
                while curr != None:
                    if curr.page == page:
                        return (curr, level, index)
                    curr = curr.next
                    index = index + 1 
                level = level.bot
        return (None, None, None)
    
    def moveUpperLayer(self, level, index):
        page, freq = level.deleteAt(index)
        if level.top == None:
            newLevel = Level(level.freq + self.max_freq)
            newLevel.insertToFront(page, freq)
            level.top = newLevel
            newLevel.bot = level
            self.tail = newLevel
        else:
            level.top.insertToFront(page, freq)
    
    def accessPage(self, page):
        curr, level, index = self.searchPage(page)
        if curr != None:
            # print('hit')
            self.hit = self.hit + 1
            curr.increment_freq()
            # print(curr.freq)
            if curr.freq > level.freq:
                self.moveUpperLayer(level, index)
            else:
                level.moveToFront(index)
        else:
            # print('miss')
            self.miss = self.miss + 1
            if self.size < self.capacity:
                self.insertToFrontOfBottomLayer(page)
            else:
                self.deleteAtLastOfBottomLayer()
                self.insertToFrontOfBottomLayer(page)

    def LRU_Op(self, ref_str, n):
        for i in range(n):
            self.accessPage(ref_str[i])
            # print("Page: ", ref_str[i])
            # self.print_cache()

    def hit_ratio(self):
        return self.hit / (self.hit + self.miss) * 100
    
    def print_cache(self):
        print("Start")
        level = self.tail
        while level != None:
            curr = level.next
            while curr != None:
                print('{} ({}) '.format(curr.page, curr.freq), end = " ")
                curr = curr.next
            print()
            level = level.bot
        print("End")

    def free_cache(self):
        level = self.tail
        while level != None:
            while level.size:
                level.deleteAt(0)
            level = level.bot

# if __name__ == '__main__':
#     capacity = 128
#     lru = LRU_SkipList(capacity)
#     ref_str = []
#     with open("input/" + "gcc" + ".trace", 'r') as inp:
#         res = inp.readlines()
#         # print(res)
#         for item in res:
#             addr = item[0:9]
#             page = int(int(addr, 16) / (4096))
#             ref_str.append(page)
#     n = len(ref_str[:100000])
#     lru.LRU_Op(ref_str[:100000], n)
#     print("Hit Ratio: ", lru.hit_ratio())
#     lru.print_cache()
