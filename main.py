for _ in range(int(input())):
    N,K,S=map(int,input().split(' '))
    l=[]
    for i in range(N):
        if S%K==0:
            l.append(0)
            S//=K
        elif S%K==1:
            l.append(1)
            S=(S-1)//K
        elif S%K==K-1:
            l.append(-1)
            S=(S+1)//K
    if S==0:
        print(*l)
    else:
        print(-2)
'''hint-Here we use the rule remainder+divisor*quotient=dividend
'''
