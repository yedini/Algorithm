h_codes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

inputs = input()

for i in range(len(h_codes)):
    if h_codes[i] == inputs[0]:
        h = i+1

v = int(inputs[1])

scenario = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

case = 0
for s in scenario:
    newh = h + s[0]
    newv = v + s[1]
    if newh >0 and newh < 9 and newv >0 and newv <9 :
        case += 1

print(case)
