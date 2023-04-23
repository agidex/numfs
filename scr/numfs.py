## NumFS - Number File System
## keep numbers in numbers
## function = x**y

import time

MAX_ITER = 1000000

##file = {
##    x = 2,
##    y = 5,
##    position = 0,
##    length = 5
##    }

def function(x, y):
    return (x + y) ** (x + y)

def find(str_to_keep):
    i = 0

    trigger = True
    x = 1
    y = 1

    time_start = time.clock()
    while(i < MAX_ITER):
        i += 1
        #print(x, y)
        s = str(function(x, y))
        #print(s)
        pos = s.find(str_to_keep)
        if (pos != -1):
            file = {
                'x'   : x,
                'y'   : y,
                'pos' : pos,
                'len' : len(str_to_keep)
                }
            print('OK, iterations = %s' % (i))
            print('Time taken: %s sec.' % (time.clock() - time_start))
            return file
        else:
            if (trigger):
                x += 1
                trigger = False
            else:
                y += 1
                trigger = True

    print('Time taken: %s sec.' % (time.clock() - time_start))
    raise OverflowError("Too many iterations!")

def create(x, y, pos, l):
    file = str(function(x, y))[pos:pos+l]
    return file

file1 = '02051992'
##file1 = '13011995'
print('initial file is: %s' % (file1))
file_stamp = find(file1)
print('file stamp is: ')
print(file_stamp)

##file_stamp = {'x': 6829, 'pos': 14034, 'y': 6829, 'len': 8}

print('give me back')
file2 = create(file_stamp['x'], file_stamp['y'], file_stamp['pos'], file_stamp['len'])
print(file2)

##def function(x, y):
##    return x ** y
##>>> 
##====================== RESTART: E:/PROG/Python/numfs.py ======================
##initial file is: 02051992
##OK, iterations = 13657
##Time taken: 108.86161704428325 sec.
##file stamp is: 
##{'pos': 14034, 'x': 6829, 'y': 6829, 'len': 8}
##give me back
##02051992
##>>> 
##====================== RESTART: E:/PROG/Python/numfs.py ======================
##initial file is: 13011995
##OK, iterations = 4036
##Time taken: 2.3382811573257745 sec.
##file stamp is: 
##{'pos': 1904, 'len': 8, 'x': 2019, 'y': 2018}
##give me back
##13011995
##>>> 


##def function(x, y):
##    return (x + y) ** (x + y)
##>>> 
##====================== RESTART: E:/PROG/Python/numfs.py ======================
##initial file is: 13011995
##OK, iterations = 6417
##Time taken: 44.6456631475174 sec.
##file stamp is: 
##{'x': 3209, 'pos': 11089, 'y': 3209, 'len': 8}
##give me back
##13011995
##>>> 
##====================== RESTART: E:/PROG/Python/numfs.py ======================
##initial file is: 02051992
##OK, iterations = 6828
##Time taken: 54.23891004831407 sec.
##file stamp is: 
##{'x': 3415, 'pos': 14034, 'y': 3414, 'len': 8}
##give me back
##02051992
##>>> 
