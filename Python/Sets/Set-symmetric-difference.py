n = int(input())
n_arr = set(map(int,input().split()))
m = int(input())
m_arr = set(map(int,input().split()))

print(len(n_arr^m_arr))
