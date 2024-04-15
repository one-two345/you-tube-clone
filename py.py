def binary_search(lis, target):
    low, high = 0, len(lis)
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    lis = []
    for num in a:
        pos = binary_search(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

    print(len(lis))
