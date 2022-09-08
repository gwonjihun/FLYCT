'''
0과, 1의 갯수를 절반으로 제거하여 새로운 문자열을 만들려고한다.
가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.
1은 앞에서부터 0은 뒤에서부터 지우기
'''

import sys
input = sys.stdin.readline

S = list(input().strip())