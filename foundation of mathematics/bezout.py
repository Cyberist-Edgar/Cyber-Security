from math import fabs

    
def bezout(a, b):
    if(a<b):
        a, b = b, a
    if(b==0):
        return 1, 0 
    
    if(b==1):
        return 0, 1

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    if (r2!=0):
        q = r1//r2
        r2, r1 = (-q)*r2+r1 , r2
    else:
        return s1, t1       

    while(r2!=0):
        s2, s1 = (-q)*s2+s1, s2
        t2, t1 = (-q)*t2+t1, t2
        q = r1//r2
        r2, r1 = (-q)*r2+r1, r2
    sympol = "+" if t2 > 0 else "-"

    print(f"{s2} * {a} {sympol} {round(fabs(t2))} * {b} = ({a}, {b})")

        
question = [(166, 332),(984, 1038),(1124, 1213),(1281, 2019),(1338, 2018),(2020, 313),
(202003, 1601),(20200310, 1231),(1301, 1373),(1601, 1681)]


for i in question:
    bezout(*i)

