inp = open("input3.txt")
#считать строку ввода, разделить и преобразовать к числам
n, q = map(int,inp.readline().split())

#массив для пар (директор, подчиненный)
eq=[]

for i in range(0, n-1):
    #считать индекс директора и подчиненного
    a, b = map(int, inp.readline().split())
    #соотнести индексу работника номер руководителя
    eq.append((a, b))

#поиск глубины элемента со значением idx в дереве
#d - начальная глубина при запуске рекурсии
def depth(tr, idx, d):
    for item in tr.items():
        if item[0] == idx:
            return d, True
        else:
            nd, stop = depth(item[1], idx, d + 1)
            if stop == True:
                return nd, True
    return d, False

#посчитать количество веток на глубине depth
#cdepth - начальная глубина при запуске рекурсии
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

#добавляет в дерево tr начальника dir и подчиненного sub
def paste(tr, dir, sub):
    for item in tr.items():
        if item[0] == dir:
            tr[item[0]][sub] = {}
            return True
    for item in tr.items():
        if paste(item[1], dir, sub):
            return True
    return False

#корень дерева - директор(индекс 1), ветки - подчиненные
tree={}

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
#крутится в цикле пока есть элементы
while len(eq) != 0:
    for x in range(0, len(eq)):
        #вставка элементов в дерево и удаление ненужной пары из списка пар
        if paste(tree, eq[x][0], eq[x][1]):
            del eq[x]
            break

#прочитать запросы    
for q in [*map(int, inp.readline().split())]:
    #для директора всегда известный вывод
    if q==1:
        print(1)
    else:
        d, _ = depth(tree, q, 0)
        print(q, d, count(tree, d, 0))
