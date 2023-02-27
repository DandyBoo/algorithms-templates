n = int(input())
sizes = sorted(list(map(int, input().split())), reverse=True)
for i in range(n - 2):
    if sizes[i] < (sizes[i + 1] + sizes[i + 2]):
        print(sizes[i] + sizes[i + 1] + sizes[i + 2])
        break
