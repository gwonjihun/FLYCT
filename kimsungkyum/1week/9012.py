n = int(input())


for _ in range(n):
    VPS = input() 
    stack = [] 
    for i in VPS:
        if i == ')':
            if stack and (stack[-1]=='('):
                stack.pop()
            else:
                stack.append(i)
        
        if i == '(':
            stack.append(i)
    
    if stack:
        print('NO')
    else:
        print('YES')
