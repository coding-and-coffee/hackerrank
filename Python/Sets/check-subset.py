n = int(input().strip())
for i in range(n):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    print(set_a.issubset(set_b))