n = 5
check = 0
for i in range(1,6):
    if n%i == 0:
        check = check +1

if check==2:
    print('true')
else:
    print('false')