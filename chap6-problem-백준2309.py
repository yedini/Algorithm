import itertools
n = []
for i in range(9):
    n.append(int(input()))

coms = list(itertools.combinations((n), 7))

for c in coms:
    sumn=[]
    for i in list(c):
        sumn.append(i)
    if sum(sumn) == 100:
        result = sorted(sumn)

for i in result:
    print(i)