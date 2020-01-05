set_a = set(input().split())
n = int(input())
for i in range(n):
    set_b = set(input().split())
    if not set_b.issubset(set_a) and len(set_b) < len(set_a):
        print(False)
        break
else:
    print(True)
