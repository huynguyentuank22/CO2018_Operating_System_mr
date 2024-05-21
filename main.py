from Bit_Used import *
from Self_Adjustable_Doubly_Circular_Link_List import *
from Splay_tree import *
from Skip_List import *
from randtest import *
from plot import *

if __name__ == '__main__':
    sz_ref_str = [1000, 10000, 25000, 50000, 100000]
    hit_rateofDCLL, hit_rateofSplayTree, hit_rateofBitUsed, hit_rateofSkipList = [], [], [], []

    cache_size = int(input("Enter the cache size: "))
    type = input("Enter the type of reference string: ")
    ref_str = inpTest(type)

    for sz in sz_ref_str:
        # print(sz, end="\n")
        lrubyDCLL = LRU_LinkList(cache_size)
        lrubySplayTree = LRU_SplayTree(cache_size)
        lrubyBitUsed = LRU_BitUsed(cache_size)
        lrubySkipList = LRU_SkipList(cache_size)

        lrubyDCLL.LRU_Op(ref_str[0:sz], sz)
        lrubySplayTree.LRU_Op(ref_str[0:sz], sz)
        lrubyBitUsed.LRU_Op(ref_str[0:sz], sz)
        lrubySkipList.LRU_Op(ref_str[0:sz], sz)

        hit_rateofDCLL.append(lrubyDCLL.hit_ratio())
        hit_rateofSplayTree.append(lrubySplayTree.hit_ratio())
        hit_rateofBitUsed.append(lrubyBitUsed.hit_ratio())
        hit_rateofSkipList.append(lrubySkipList.hit_ratio())

        lrubyDCLL.free_cache()
        lrubySplayTree.free_cache()
        lrubyBitUsed.free_cache()
        lrubySkipList.free_cache()
        
    
    # with open("output.txt", 'w') as out:
    #     out.write(str(ref_str) + "\n")
    #     lrubyDCLL.LRU_Op(ref_str, len(ref_str))
    #     lrubySplayTree.LRU_Op(ref_str, len(ref_str))
    #     lrubyBitUsed.LRU_Op(ref_str, len(ref_str))
    #     out.write("Hit ratio of DCLL: " + str(lrubyDCLL.hit_ratio())+"\n")
    #     out.write("Hit ratio of SplayTree: " + str( lrubySplayTree.hit_ratio())+"\n")
    #     out.write("Hit ratio of BitUsed: " + str(lrubyBitUsed.hit_ratio())+"\n")
    hit_res = {
        "DCLL": hit_rateofDCLL,
        "SplayTree": hit_rateofSplayTree,
        "BitUsed": hit_rateofBitUsed,
        "SkipList": hit_rateofSkipList
    }
    plot_result(hit_res, sz_ref_str, cache_size, type, sz_ref_str)
        