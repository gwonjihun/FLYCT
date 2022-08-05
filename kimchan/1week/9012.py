'''
괄호
문제의 핵심은 (로 열어서 )로 잘 닫혔는지 확인해야 한다.
만약 잘 닫혔다면 YES를 반환, 아니면 NO를 반환
''' 

import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    datas = input().strip()
    check = {}
    # ( )의 개수를 딕셔너리로 저장
    for data in datas:
        if data not in check:
            check[data] = 1
        else:
            check[data] += 1

    # '('만 들어있거나 ')'만 들어있다면
    if len(check.values()) == 1:
        print("NO")
        continue # 아래 코드 실행 안하고 다음 for문 실행

    # ( )의 개수가 같다면
    if check['('] == check[')']:
        while ("()" in datas):
            datas = datas.replace("()", "")
        if datas == "":
            print("YES")
        else: 
            print("NO")
    # ( )의 개수가 같지 않다면 무조건 NO
    else:
        print("NO")