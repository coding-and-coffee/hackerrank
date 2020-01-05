n,m = map(int,input().split())
n_arr = input().split()
a = set(input().split())
b = set(input().split())
happy = 0
for x in n_arr:
    happy += sum([(x in a) - (x in b)])
print(happy)