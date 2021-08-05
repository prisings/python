n = 5

for i in range(n):
    for j in range(n):
        if j <= i:
            print("*",end='')
    print()

for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))
