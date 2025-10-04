# ()()
# (())

# 위 두가지를 모두 판별할 수 있어야 함
# ')'이 들어오면 앞에는 '('이 하나라도 있어야 한다.
# 존재한다면 '('을 하나 제거 , 없으면 return False로 반환
# queue, stack

def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        if s[i] == ')':
            if stack and stack.pop() == '(':
                continue
            else:
                answer = False
                break
    if len(stack) > 0:
        answer = False

    return answer

