def euclid(a,b):
    """
    计算欧几里得除法，求a对b的不完全商q和余数r
    """
    q = 0
    r = a
    temp = a
    while(temp>=b):
        q += 1
        temp = temp-b
    r = temp
    return f"a = {q}*{b}+{r}"

def euclid2(a,b):
    """
    直接使用公式 q=[a/b], r=a-[a/b]*b
    """
    return f"a = {a//b}*{b}+{a%b}"

import time
start = time.time()

print(euclid2(509090,38))

end = time.time()

print(f"Cost: {end-start}")

        
        
        


        
