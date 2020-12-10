n, q = map(int,input().split())
eq=[]

for i in range(0, n-1):
    a, b = map(int, input().split())
    eq.append((a, b))

def depth(tr, idx, d):
    for item in tr.items():
        if item[0] == idx:
            return d, True
        else:
            nd, stop = depth(item[1], idx, d + 1)
            if stop == True:
                return nd, True
    return d, False

def count(tr, depth, cdepth):
    if cdepth < depth:
        x = 0
        for item in tr.items():
            x += count(item[1], depth, cdepth + 1)
        return x
    else:
        x = 0
        for item in tr.items():
            x += 1
        return x

def paste(tr, dir, sub):
    for item in tr.items():
        if item[0] == dir:
            tr[item[0]][sub] = {}
            return True
    for item in tr.items():
        if paste(item[1], dir, sub):
            return True
    return False

tree={}

removed = True
while removed == True:
    removed = False
    for x in range(0, len(eq)):
        if eq[x][0] == 1:
            tree[eq[x][1]]={}
            del eq[x]
            removed = True
            break

while len(eq) != 0:
    for x in range(0, len(eq)):
        if paste(tree, eq[x][0], eq[x][1]):
            del eq[x]
            break

for q in [*map(int, input().split())]:
    if q==1:
        print(1)
    else:
        d, _ = depth(tree, q, 0)
        print(count(tree, d, 0))
