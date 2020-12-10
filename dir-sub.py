"""
#считать строку ввода, разделить и преобразовать к числам
n, q = map(int,input().split())
#создать пустой список длины n
eq=[[] for i in range(0, n)]
for i in range(0, n-1):
    #считать индекс директора и подчиненного
    a, b = map(int, input().split())
    #соотнести индексу работника номер руководителя
    eq[b-1].append(a)
#прочитать запросы    
for q in [*map(int, input().split())]:
    #для директора всегда известный вывод
    if q==1:
        print(1)
    else:
        #найти номер руководителя для работника
        z=eq[q-1]
        #посчитать количество людей с тем же директором
        i = 0
        for x in eq:
            if x == z:
                i+=1
        print(i)
"""

"""
10 4
3 2
6 4
5 3
1 6
8 7
10 8
10 9
1 6
1 10
"""

inp = open("input3.txt")
#считать строку ввода, разделить и преобразовать к числам
n, q = map(int,inp.readline().split())

#создать пустой список длины n
eq=[]

for i in range(0, n-1):
    #считать индекс директора и подчиненного
    a, b = map(int, inp.readline().split())
    #соотнести индексу работника номер руководителя
    eq.append((a, b))

print("eq", eq)
#tree = {}
tree1={
    10:{ 8:{7:{}},
        10:{9:{}}},
    5:{3:{2:{}}},
    6:{4:{}}
}
print("tree", tree1)

tree={}

def walk(tr, idx, num):
    if len(tr) == 0:
        return num
    for item in tr.items():
        walk(item[1], idx, num)
    for item in tr.items():
        print(item)
        if item[1] == idx:
            return num + 1
    return num

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
    
    
    """
    if depth == 0:
        for item in tr.items():
            num += 1
        return num
    else:
        x = num
        for item in tr.items():
            x += count(item[1], depth + 1, num)
        return x
    """

#рекурсивно ищет место и добавляет в дерево tr начальника dir и подчиненного sub
def paste(tr, dir, sub):
    #if len(tr) == 0 or len(tr) == 1:
    if len(tr) == 0:
        return False
    print("paste", tr)
    for item in tr.items():
        if item[0] == dir:
            tr[item[0]][sub] = {}
            return True
    for item in tr.items():
        print("item", item)
        if paste(item[1], dir, sub) == True:
            return True
    return False

print("walk")
#walk(tree1)

print("-----------")
print(eq)

#заполнение уровня дерева вокруг директора
removed = True
while removed == True:
    removed = False
    for x in range(0, len(eq)):
        if eq[x][0] == 1:
            tree[eq[x][1]]={}
            del eq[x]
            removed = True
            break
        
#заполнение остальной части дерева
#while len(eq) != 0:
print("eq", eq)
print("tree", tree)

while len(eq) != 0:
    for x in range(0, len(eq)):
        pasted = paste(tree, eq[x][0], eq[x][1])
        print(pasted)
        print("len(eq)", len(eq))
        print(eq)
        if pasted:
            del eq[x]
            break

print("eq", eq)
print("tree", tree)
#exit(0)

#прочитать запросы    
for q in [*map(int, inp.readline().split())]:
    #для директора всегда известный вывод
    if q==1:
        print(1)
    else:
        #num = walk(tree, q, 0)
        d, _ = depth(tree, q, 0)
        #print(q, d)
        print(q, d, count(tree, d, 0))
