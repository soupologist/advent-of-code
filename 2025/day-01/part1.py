N = 4412

arr = []

for i in range(N):
    arr.append(input())

# print(arr)

curr = 50

res = 0
for i in range(len(arr)):
    
    direction, val = arr[i][0], int(arr[i][1:])
    # print(direction, val)
    
    if direction == 'L':
        curr = (curr - val) % 100
    else:
        curr = (curr + val) % 100
    
    if curr == 0:
        res += 1

print(res)
    
    
    