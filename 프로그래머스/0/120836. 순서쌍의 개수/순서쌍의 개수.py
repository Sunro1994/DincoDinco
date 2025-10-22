def solution(n):
    num = 0
    # n의 약수의 개수를 구해라
    for i in range(1, n//2+1):
        if n%i == 0:
            num +=1
    return num+1