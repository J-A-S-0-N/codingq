#Your mission here is to create a function that gets a tuple and returns a tuple with 
#3 elements - the first, third and second element from the last for the given array.

def easy_unpack(a,b,c,d,e,f,g,h):
    l = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)
    ll = list(l)
    la = ll[0]
    lb = ll[2]
    lc = ll[1]
    print(la,lb,lc)
easy_unpack(4, 3, 5, 4, 5, 3, 7, 1)
#easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#easy_unpack((6, 3, 7)) == (6, 7, 3)