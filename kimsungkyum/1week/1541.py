exp = input()

nums = [] # 숫자가 저장될 리스트
symbols = [] # 기호가 저장될 리스트 

temp = [] # 숫자를 임시로 저장할 리스트
for i in exp:
    if i == '-' or i == '+': # 수학 기호가 나오면 분리
        nums.append(int(''.join(temp))) # 리스트를 하나의 숫자로 병합하여 저장
        symbols.append(i)
        temp = []
        continue
    temp.append(i)
nums.append(int(''.join(temp))) #남아있는 마지막 숫자 저장

result = 0 # 결과를 저장할 변수

idx = -1
for i in range(len(symbols)): # 첫번재 '-' 기호를 저장
    if symbols[i] == '-':
        idx = i
        break

if idx == -1: # '-' 기호가 없을 경우
    result = sum(nums)
else:  
    result = sum(nums[:idx+1]) - sum(nums[idx+1:])
print(result)