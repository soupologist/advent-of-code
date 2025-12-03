def check_repetition(num: str):
    if len(num) % 2 != 0:
        return False
    l, r = 0, len(num) // 2
    
    for l in range(len(num) // 2):
        # print(l, r)
        if num[l] != num[r]:
            return False
        r += 1
    return True

ranges = input().split(',')

res = 0

for r in ranges:
    left, right = r.split('-')
    left, right = int(left), int(right)
    
    for n in range(left, right + 1):
        if check_repetition(str(n)):
            # print(n)
            res += n
print(res)
    