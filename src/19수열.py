#등차
n = int(input("n"))

a = 3

for i in range(n-1):
    a = a+5

print(a)

#등비
a = 3

for i in range(n-1):
    a = a*2

print(a)

#피보나치

n = int(input("n"))
a = 1
b = 1

for i in range(n-2):
    c = a+b
    a = b
    b = c

print(c)