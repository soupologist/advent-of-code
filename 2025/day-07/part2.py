# N = 16
N = 142

from functools import lru_cache

@lru_cache(None)
def descend(r, c):
    
    while r < N and arr[r][c] != '^':
        r += 1
        
    if r == N:
        res = [0] * M
        res[c] += 1
        return res
    
    left = descend(r + 1, c - 1) if c > 0 else [0] * M
    right = descend(r + 1, c + 1) if c < M - 1 else [0] * M
    return [left[i] + right[i] for i in range(M)]

arr = []
for i in range(N):
    arr.append(list(input()))

M = len(arr[0])
print(N, M)


start = -1
for i in range(M):
    if arr[0][i] == 'S':
        start = i
        break
print(start)


final = descend(0, start)
print(final)
print(sum(final))