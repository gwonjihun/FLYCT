func = input().split('-') # 식을 입력받는다. (- 사이의 식들에 괄호를 치는 것 처럼 하기 위함.)

nums = [] # 식에서 숫자를 임시로 저장할 빈 리스트를 생성

for num in func: 
    sum_result = 0 # 더한 값을 저장할 변수 (반복문이 시작할 때마다 초기화)

    s_nums = num.split('+') # '+'가 있으면 '+'기준으로 숫자를 나눈다.

    for s_num in s_nums: # 나뉘어진 값들을 반복문을 사용하여 더한다.

        sum_result += int(s_num) # s_num값은 원래 문자열이기 때문에 int로 형변환 후 더해야함.

    nums.append(sum_result) # 더해진 값을 배열에 추가

result = nums[0] # nums에 저장된 값 맨 앞부터 빼주기 위해 '0' 인덱스의 값을 result에 저장

for index in range(1, len(nums)): #nums에 모든 값들을 빼주면서 result 업데이트
    result -= nums[index]
    
print(result) # 출력

