input_d = input()
r = int(input_d[1])
c = int(ord(input_d[0]) - int(ord('a')))+1


directions = ['L','R','U','D']
dc = [-1,1,0,0]
dr = [0,0,-1,1]


count = 0

move_types = [['L','L','U'],['L','L','D'],['R','R','U'],['R','R','D'],
              ['U','U','L'],['U','U','R'],['D','D','L'],['D','D','R']]

for move in move_types:
    nc = c
    nr = r
    for i in move:
        for d in range(len(directions)):
            if i == directions[d]:
                nc = nc + dc[d]
                nr = nr + dr[d]
            
    if nc >= 1 and nc <= 8 and nr >= 1 and nr <= 8:
        count += 1
            
print(count)