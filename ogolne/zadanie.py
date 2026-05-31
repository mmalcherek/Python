# n=int(input('ile razy?: '))
# for i in range(0,n+1):
#     for j in range(0,i):
#         print("*", end='')
#     print('\r')
n=5

for  i in range(0,n):
    for j in range(0,n-i):
            print(end=' ')
    for j in range(0,i+1):
            print('*', end='')
    for j in range(0,n+(i-n)):
            print('*', end='')
    print('\r')

