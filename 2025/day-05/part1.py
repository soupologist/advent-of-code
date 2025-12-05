N, M = 172, 1000

intervals = []

for i in range(N):
    temp = input().split('-')
    intervals.append([int(temp[0]), int(temp[1])])
    
intervals.sort()
final = [intervals[0]]

for start, end in intervals[1:]:
    lastEnd = final[-1][1]
    
    if start <= lastEnd:
        final[-1][1] = max(lastEnd, end)
    else:
        final.append([start, end])

# print(final)

input()

res = 0

for i in range(M):
    
    val = int(input())
    
    flag = 0
    for l, r in final:
        if l <= val <= r:
            flag = 1
            break
    
    if flag:
        res += 1

print(res)


    