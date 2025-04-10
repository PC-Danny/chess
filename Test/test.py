moveslist = [(-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

def sqdist(vector):
    return sum(x*x for x in vector)

moveslist.sort(key=sqdist)

moveslist
# print(moveslist)

[(-7, 0), (-6, 0)] + [(-5, 0), (-4, 0)]

movesQueen = [(-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (-7, -7), (-7, 7), (-6, -6), (-6, 6), (-5, -5), (-5, 5), (-4, -4), (-4, 4), (-3, -3), (-3, 3), (-2, -2), (-2, 2), (-1, -1), (-1, 1), (1, -1), (1, 1), (2, -2), (2, 2), (3, -3), (3, 3), (4, -4), (4, 4), (5, -5), (5, 5), (6, -6), (6, 6), (7, -7), (7, 7)]
movesQueen.sort(key=sqdist)

print(movesQueen)
print(len(movesQueen))

class test():
    pass

a = test()

# for i in movesQueen:
#     if i[0] == 0:

#SOLUTION 1
#   
movesN = [i for i in movesQueen if i[0] == 0 and i[1] > 0]
movesNE = [i for i in movesQueen if i[0] == i[1] and i[1] > 0 ]
movesE = [i for i in movesQueen if i[0] > 0 and i[1] == 0]
movesSE = [i for i in movesQueen if abs(i[0]) == abs(i[1]) and i[0] > 0 and i[1] < 0]
movesS = [i for i in movesQueen if i[0] == 0 and i[1] < 0]
movesSW = [i for i in movesQueen if i[0] == i[1] and i[1] < 0 ]
movesW = [i for i in movesQueen if i[0] < 0 and i[1] == 0]
movesNW = [i for i in movesQueen if i[0] == i[1] and i[0] < 0]

print(len(movesN))
print(len(movesNE))
print(len(movesE))
print(len(movesSE))
print(len(movesS))
print(len(movesSW))
print(len(movesW))
print(len(movesNW))

testfunc = lambda i:  i[0] == 0 and i[1] > 0

[i for i in movesQueen if testfunc(i)]

movesQueen = [(-7, 0), (-6, 0), (-5, 0), (-4, 0), (-3, 0), (-2, 0), (-1, 0), (0, -7), (0, -6), (0, -5), (0, -4), (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (-7, -7), (-7, 7), (-6, -6), (-6, 6), (-5, -5), (-5, 5), (-4, -4), (-4, 4), (-3, -3), (-3, 3), (-2, -2), (-2, 2), (-1, -1), (-1, 1), (1, -1), (1, 1), (2, -2), (2, 2), (3, -3), (3, 3), (4, -4), (4, 4), (5, -5), (5, 5), (6, -6), (6, 6), (7, -7), (7, 7)]

moveLambdas = [lambda i: i[0] == 0 and i[1] > 0, 
         lambda i: i[0] == i[1] and i[1] > 0 , 
         lambda i: i[0] > 0 and i[1] == 0, 
         lambda i: abs(i[0]) == abs(i[1]) and i[0] > 0 and i[1] < 0, 
         lambda i: i[0] == 0 and i[1] < 0, 
         lambda i: i[0] == i[1] and i[1] < 0, 
         lambda i: i[0] < 0 and i[1] == 0, 
         lambda i: i[0] == i[1] and i[0] < 0]

directionVectors = ['movesN',
                    'movesNE',
                    'movesE',
                    'movesSE',
                    'movesS',
                    'movesSW',
                    'movesW',
                    'movesNW']

for d, l in zip(directionVectors,moveLambdas):
    globals()[d] = [i for i in movesQueen if l(i)]

### TESTING ARRAYS AND CONDITIONS
import numpy as np
testarray = [7,7]

if 8 >= 8 or 8 <= 0:
    print('passes')
else:
    print('nope')

### testing lists
import numpy as np
[np.array([0,2]),np.array([0,1])] * np.array([0,-1])

(lambda list : [list[0],list[1]*-1])([0,1])
