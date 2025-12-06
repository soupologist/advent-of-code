N = 5

arr = []
for i in range(N - 1):
    arr.append(list(map(int, input().split())))
    
ops = input().split()

for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if ops[j] == '+':
            arr[0][j] += arr[i][j]
        else:
            arr[0][j] *= arr[i][j]

print(arr[0])
print(sum(arr[0]))
