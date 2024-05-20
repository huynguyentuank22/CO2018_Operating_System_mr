from Bit_Used import *
from Self_Adjustable_Doubly_Circular_Link_List import *
from Splay_tree import *
from Skip_List import *
from randtest import *
from plot import *
if __name__ == '__main__':
    # cap = [8,16,32,64,128,256]
    # lrubyDCLL = LRU_LinkList(128)
    # lrubySplayTree = LRU_SplayTree(128)
    # lrubyBitUsed = LRU_BitUsed(128)
    sz_ref_str = [1000, 10000, 25000, 50000, 100000]

    hit_rateofDCLL, hit_rateofSplayTree, hit_rateofBitUsed = [], [], []
    ref_str = []
    for sz in sz_ref_str:
        # print(sz, end="\n")
        ref_str = randTest(sz, 256, ref_str)
        lrubyDCLL = LRU_LinkList(256)
        lrubySplayTree = LRU_SplayTree(256)
        lrubyBitUsed = LRU_BitUsed(256)
        lrubyDCLL.LRU_Op(ref_str, len(ref_str))
        lrubySplayTree.LRU_Op(ref_str, len(ref_str))
        lrubyBitUsed.LRU_Op(ref_str, len(ref_str))
        hit_rateofDCLL.append(lrubyDCLL.hit_ratio()*100)
        hit_rateofSplayTree.append(lrubySplayTree.hit_ratio()*100)
        hit_rateofBitUsed.append(lrubyBitUsed.hit_ratio()*100)
        
    
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
        "BitUsed": hit_rateofBitUsed
    }
    plot_result(hit_res, sz_ref_str)
        