import random
def randTest(n, sz, ref_str):
    random.seed(1)
    remain = n - len(ref_str)
    for i in range (remain):
        ref_str.append(random.randint(0, sz*2))
    
    return ref_str
    

    