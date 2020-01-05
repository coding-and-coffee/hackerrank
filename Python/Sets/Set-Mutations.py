a = int(input())
a_arr = set(map(int,input().split()))
n = int(input())
for _ in range(n):
    opp, l = input().split()
    new_arr = set(map(int,input().split()))
    eval("a_arr."+opp+"(new_arr)")
print(sum(a_arr))
