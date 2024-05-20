import pandas as pd

class Entry:
    def __init__(self):
        self.valid = False
        self.used = False
        self.page = -1


class LRU_BitUsed:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = [Entry() for _ in range(capacity)]
        self.hit = 0
        self.miss = 0
        
    def write(self, page):
        full_entry = True
        for entry in self.entries:
            if entry.valid == False:
                entry.valid = True
                entry.used = True
                entry.page = page
                full_entry = False
                break
        if full_entry:
            for entry in self.entries:
                if entry.used == False:
                    entry.valid = True
                    entry.used = True
                    entry.page = page
                    break
        for entry in self.entries:
            if entry.used == False:
                return
        for entry in self.entries:
            entry.used = False
        
    def read(self, page):
        for entry in self.entries:
            if entry.valid == True and entry.page == page:
                entry.used = True
                return True
        return False

    def print_Cache(self):
        data = {'Valid': [entry.valid for entry in self.entries],
                'Used': [entry.used for entry in self.entries],
                'Page': [entry.page for entry in self.entries]}
        df = pd.DataFrame(data)
        print(df)

    def accessPage(self, page):
        if self.read(page):
            self.hit = self.hit + 1
        else:
            self.miss = self.miss + 1
            self.write(page)

    def LRU_Op(self, arr, n):
        for i in range(n):
            self.accessPage(arr[i])
            # print("Access Page: ", arr[i])
            # self.print_Cache()

    def hit_ratio(self):
        return self.hit / (self.hit + self.miss)
    
# if __name__ == '__main__':
#     capacity = 4
#     arr = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
#     n = len(arr)
#     lru = LRU_BitUsed(capacity)
#     lru.LRU_Op(arr, n)
#     print("Hit Ratio: ", lru.hit_ratio())