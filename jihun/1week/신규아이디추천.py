def solution(new_id):
    new_id = list(new_id.lower()) # 1단계
    print("1: ", new_id)
    spe_char = ['-','_','.']
    for a in range(0,len(new_id)): # 2단계
        
        if  new_id[a].isalnum()==True or new_id[a] in spe_char :
            continue
        new_id[a]=""
    new_id = "".join(new_id)
    print("2: ", new_id)
    while ".." in new_id:
        new_id = new_id.replace("..",".")    
    print("3:",new_id)
    new_id = new_id.strip(".") #4단계
    print("4: ", new_id)
    new_id = list(new_id)
    if new_id ==[]: # 5단계
        new_id ='a'
    print("5: ", new_id)
    if len(new_id)>=16 :
        new_id = new_id[:15]   
        while new_id[-1] =='.':
            new_id= new_id[:-1] 
    print("6: ", new_id)
    while len(new_id)<=2:
        print(new_id)
        new_id = list(new_id)
        new_id+= new_id[-1]
    print("7: ", new_id)

    answer="".join(new_id)
    return answer


new_id = "=.="
a = solution(new_id)

print("answer:",a)