# import random
# def randTest(n, sz, ref_str):
#     random.seed(1)
#     remain = n - len(ref_str)
#     for i in range (remain):
#         ref_str.append(random.randint(0, sz*2))
#     return ref_str

def inpTest(type):
    ref_str = []
    with open("input/" + type + ".trace", 'r') as inp:
        res = inp.readlines()
        # print(res)
        for item in res:
            addr = item[0:9]
            page = int(int(addr, 16) / (4096))
            ref_str.append(page)
    return ref_str
    