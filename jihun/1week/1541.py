# 예를 들어서
# -50 +40 - 60 +50
# 최소가 되기 위해서는 결론적으로 + - +++++ -++++ 일때
# - 부터 -가 나오기 전까지를 괄호로 묵으면 최소가 된다
# 최대 5자
# 결론으로는 test case : 12 + 32 - 42+ 42+ 42- 42+ 42 - 42
#  1. +로 분할
# 2. -로 분할
# 최종 풀이 접근 방법
# - 수식에서 -다음 숫자부터 -이전의 숫자까지를 괄호로 포함하게되면
# - 자연스럽게 최소값으로 진행이된다.
# - 그리고 문자열을 수식으로 계산해주는 method인 eval을 활용하여 해결
# - 진행 과정에서 해결 못했던 테스트 케이스 :
# 1. 0으로 시작하는 문자열 -> lstrip으로 해결해줌
# 2. lstrip의 사용으로 인한 문제 -> 000이면 해당 값이 없기때문에 문제 발생
#import sys
#input = sys.stdin.readline
# 여기서 알게된 점 strip method는 문자열 내부의 공백을 제거하는 것이 아니라
# 문자열 시작과 끝의 공백만을 제거한다.
while 1:
    inputs = input().replace(" ","")
    inputs = inputs.split("-")

    for a in range(0,len(inputs)):
        print("1:",a)
        inputs[a] = inputs[a].lstrip("0")
        if inputs[a]=="":
            print("3:",a)
            inputs[a] += "0"
            print("4:",inputs[a])
        #여기서 +로 구성되어있는 녀석들을 전부다 전환한다면?
        temp = inputs[a].split("+")
        if len(inputs[a].split("+"))>=2:
            for i in range(0,len(temp)):
                temp[i] = temp[i].lstrip
                if temp[i]=="":
                    temp[i]="0"
            inputs[a] = "+".join(temp)         
        print("2:",inputs[a])        


    result = []
    for a in inputs:
        result.append( "("+a+")")

    result = "-".join(result)
    print(result)
    print(eval(result))