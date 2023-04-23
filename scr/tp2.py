NZ = 3

def to_lst(s):
    l = []
    for c in s:
        l.append(str(ord(c)).zfill(NZ))
    ll = ''.join(l)
    lll = [int(cc) for cc in ll]
    return lll

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def from_lst(l):
    ll = list(divide_chunks(l, NZ))
    s = []
    for item in ll:
        num = int(''.join([str(c) for c in item]))
        s.append(chr(num))
    return ''.join(s)

def long_div(a, b, n):
    l = []
    while(len(l) < n):
        div, mod = divmod(a, b)
        l.append(div)
        a = mod * 10
    return l

def match(l1, l2):
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return i
    return -1


def find(orig):
    pass


print(match([0, 9, 7, 0, 9, 8, 0, 9, 9, 1, 0, 0, 1, 0, 1, 1, 0, 2],[0, 9, 7, 0, 9, 8, 0, 9, 8, 4, 0, 4, 2, 5, 5, 3, 1, 9]))
    

orig = 'abcdef'
aa = to_lst(orig)
print(aa)
bb = long_div(547633276,564000000,18)
print(bb)
print(from_lst(aa))
print(from_lst(bb))


