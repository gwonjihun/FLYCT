n = list(input())
i=0
start = 0
while i<len(n):
    if n[i]=="<":
        i+=1
        while n[i]!=">":
            i+=1
        i+=1
    elif n[i].isalnum():
        start=i
        while i<len(n) and n[i].isalnum():
            i+=1
        temp = n[start:i]
        temp.reverse()
        n[start:i]= temp
    else:
        i+=1
print("".join(n))