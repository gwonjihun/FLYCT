# [백준 1541] 잃어버린 괄호
'''
문제
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

입력
첫째 줄에 식이 주어진다. 
식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

출력
첫째 줄에 정답을 출력한다.
'''

# Solution 1. + 를 - 로 최대한 replace하여 연산하는 방법
import sys
# 입력받은 식
question = sys.stdin.readline().rstrip()
# 숫자 리스트 & 숫자 & 연산
numbers, num, operations = list(), '', ''
for i, c in enumerate(question):
    if c.isdigit(): # 문자가 숫자면
        num += c
    else:
        operations += c # 연산기호 리스트에 추가
        numbers.append(int(num)) # 숫자 리스트에 추가
        num = '' # 숫자 초기화
    if i == len(question)-1: # 마지막 숫자면 숫자 리스트에 추가
        numbers.append(int(num))

# + 연산을 최대한 - 연산으로 바꾸기
idx = operations.find('-')
if idx != -1: # 첫 - 이후의 + 는 - 연산으로 replace 가능 ex. -(1+2) => -1-2
    operations = operations[:idx] + operations[idx:].replace('+', '-')

# 값이 최소가 되는 식 계산하기
answer = numbers[0]
for i, op in enumerate(operations, start=1):
    if op == '-':
        answer -= numbers[i]
    else:
        answer += numbers[i]

print(answer)


'''
# Solution 2. split 이용하여 연산하는 방법
import sys
# 입력받은 식
question = sys.stdin.readline().rstrip()
# - 를 기준으로 식 나누기
numbers = question.split('-')
answer = 0
for num in numbers:
    # + 연산 (괄호 연산)
    plus = sum(map(int, num.split('+')))
    if answer == 0: # 첫 번째 연산이면
        answer = plus
    else: # 다음 연산 값들 - 처리
        answer -= plus
print(answer)
'''