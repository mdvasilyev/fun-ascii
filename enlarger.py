n=int(input())
for i in eval(input()):print(((''.join(j*n for j in i)+'\n')*n)[:-1])