# N = 16
N = 142

arr = []
for i in range(N):
    arr.append(list(input()))

M = len(arr[0])

print(N, M)

splits = set()
descended = set()

start = -1
for i in range(M):
    if arr[0][i] == 'S':
        start = i
        break

print(start)

def descend(r, c):
    
    descended.add((r, c))
    
    while r < N and arr[r][c] != '^':
        r += 1
    
    if r == N:
        return
    elif arr[r][c] == '^':
        splits.add((r, c))
        
        if (r + 1, c - 1) not in descended:
            descend(r + 1, c - 1)
        if (r + 1, c + 1) not in descended:
            descend(r + 1, c + 1)

descend(0, start)

# print(splits)
print(len(splits))