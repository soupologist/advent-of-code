N = 4412
# N = 10

arr = []

for i in range(N):
    arr.append(input())

# print(arr)

curr = 50
res = 0

for i in range(len(arr)):
    
    direction, val = arr[i][0], int(arr[i][1:])
    if val > 100:
        res += (val // 100)
        val = (val % 100)
    # print(direction, val)
    
    if direction == 'L':
        
        if curr == 0:
            curr = 100
        curr -= val
        
        if curr < 0:
            curr += 100
            res += 1
            
    else:
    
        curr += val
        
        if curr > 100:
            curr -= 100
            res += 1
        if curr == 100:
            curr = 0
    
    if curr == 0:
        res += 1
    print(direction, val, curr, res)

print(res)
    
    
    