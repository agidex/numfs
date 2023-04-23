# toothpin chonicle




#65-90

text = 'ARCHIVE'

def text2array(text):
    a = [str(ord(c)) for c in text]
    b = [int(c) for c in ''.join(a)]
    return b

arr = text2array(text)

print(arr)


base = 5761
point = 775

print(point/base)
print(0.65826772738669)
print('=======')

def longdiv(a, b, l):
    result = []
    while len(result) < l + 1:
        if a < b:
            result.append(0)
            a *= 10
        else:
            result.append(a // b)
            a = a % b * 10
    return result

def printable(longnumber):
    long = ['0.']
    long.extend([str(c) for c in longnumber[1:]])
    return ''.join(long)

print(point/base)
print(printable(longdiv(point, base, 15000)))


