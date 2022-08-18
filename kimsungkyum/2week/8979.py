n,k = map(int, input().split())

nations = []

for i in range(n):
    score = list(map(int, input().split())) + [i+1]
    nations.append(score)

#print(nations)

for i in reversed(range(4)):
    nations.sort(key=lambda x:x[i], reverse=True)

for i in range(n):
    if nations[i][4] == k:
        print(i+1)
        break