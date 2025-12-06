N = 5
M = 3744

arr = []
for i in range(N - 1):
    arr.append(input())
ops = input().split()

print(len(arr[0]))
print(ops, len(ops))

arr_transpose = [[arr[j][i] for j in range(N - 1)] for i in range(M)]

final = [[] for _ in range(len(ops))]

j = 0
for i in range(len(arr_transpose)):
    temp = "".join(arr_transpose[i])
    print(temp, j, final)

    if temp.strip() == '':
        j += 1
    else:
        final[j].append(int(temp))

print(final)

res = []

for i in range(len(ops)):

    if ops[i] == '+':
        curr = sum(final[i])
        res.append(curr)

    elif ops[i] == '*':
        curr = 1
        for val in final[i]:
            curr *= val
        res.append(curr)

print(res)
print(sum(res))