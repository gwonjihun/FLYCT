N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            result-=1
            break
print(result)

# 간단하게 해결했다. 
# 접근 방식은 aabba를 예시로 생각해서 문제 해결을 진행했고
# aa가 접근 뒤에 a가 등장하면 그룹문자가 아닌것임을 통해서
# 문제를 해결
#
#