import os
fn = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
print(fn)

i = open(fn).read()

sl = 25 * 6
nl = len(i) / sl

#phase1

n0 = sl
n1 = 0
n2 = 0
for j in range(100):
    l = i[j*sl:j*sl+sl]
    k = l.count('0')
    if k < n0:
        n0, n1, n2 = k, l.count('1'), l.count('2')
        print(n0,n1,n2,n1*n2)
        
print()
m = list(" " * 150)

#phase2

for j in reversed(range(100)):
    l = i[j*sl:j*sl+sl]
    for k in range(len(l)):
        if l[k] == '0':
            m[k] = ' '
        if l[k] == '1':
            m[k] = 'X'
        
for j in range(6):
    print(''.join(m[j*25:j*25+25]))