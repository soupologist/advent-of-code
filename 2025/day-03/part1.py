N = 200

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

res = 0

for bank in arr:
    temp = [bank[-1] for _ in range(len(bank))]
    
    for i in range(len(bank) - 2, -1, -1):
        temp[i] = max(temp[i + 1], bank[i + 1])
    temp.pop()
    bank.pop()
        
    curr = 0
    for a, b in zip(bank, temp):
        val = int(str(str(a) + str(b)))
        # print(a, b, val, curr)
        if val > curr:
            curr = val
    res += curr
    # print(curr)

print(res)
    
    
