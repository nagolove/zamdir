n, q = map(int,input().split())
eq=[[] for i in range(0, n)]
for i in range(0, n-1):
    a, b = map(int, input().split())
    eq[b-1].append(a)
for q in [*map(int, input().split())]:
    if q==1:
        print(1)
    else:
        z=eq[q-1]
        i = 0
        for x in eq:
            if x == z:
                i+=1
        print(i)
