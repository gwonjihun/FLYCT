
l = list(map(int, input())) 

size = len(l)/2
zero = 0
one = 0 
print(size, zero, one, l)
for i in range(len(l)):
    while True: 
        if zero == len and one == len:
            print(l)
            break
        if l[i] == 0:
            zero+=1
            del l[i]
        else:
            one += 1
            del l[i] 