numTests = int(input())
for i in range(numTests):
    num, limit = map(int, input().split())
    values = sorted(list(map(int, input().split())))
    count = 0
    while count<len(values) and values[count] <= limit:
            limit -= values[count]
            count += 1
    print("Case #{}: {}".format(i+1, count))
