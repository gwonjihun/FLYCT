n = input().replace(" ","")

n = n.split("-")

for a in range(0,len(n)):
    n[a] = n[a].lstrip("0")
    if n[a] == "":
        n[a] = "0"
    if n[a].find("+")!=-1:
#        print("n[a] : ", n[a])
        temp = n[a]
        temp = temp.split('+')
        for s in range(0,len(temp)):
            temp[s] = temp[s].lstrip("0")
            if temp[s] =="":
                temp[s] = "0"
        temp = "+".join(temp)
#        print("temp:",temp)
        n[a] = temp

result = []
for a in n:
    result.append("("+a+")")

temps = "-".join(result)
print(eval(temps))