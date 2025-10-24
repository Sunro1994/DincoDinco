def solution(n):
    for i in range(1, n+1):
        answer = [n]
        while True:
            if i==1:
                break
            if i%2==0:
                i//=2
                answer.append(i)
            else:
                i = 3*i+1
                answer.append(i)
    return answer