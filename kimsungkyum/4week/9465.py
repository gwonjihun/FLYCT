# 실패....

n = int(input())


for i in range(n): 
    num = int(input())
    temp1 = list(map(int, input().split())) 
    temp2 = list(map(int, input().split()))
    stickers = [0]*num + temp1+temp2 + [0]*num
    #print(stickers)
    res = 0 
    while sum(stickers) != 0 :
        ind = stickers.index(max(stickers))
        #print(ind, stickers[ind])
        res += stickers[ind]
        stickers[ind] = 0
        stickers[ind+num] = 0
        stickers[ind-num] = 0
        stickers[ind-1] = 0 
        stickers[ind+1] = 0
    print(res)
        