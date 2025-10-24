def solution(N, number):
    # N과 number가 같으면 1번만 사용하면 됨
    if N == number:
        return 1
    
    # 1. DP 테이블 초기화 (set을 담는 리스트)
    # dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]
    
    # 2. 반복을 통해 DP 테이블 채우기
    # i는 N의 사용 횟수
    for i in range(1, 9):
        # 2-A. N을 i번 이어 붙인 수 추가 (예: 5, 55, 555...)
        dp[i].add(int(str(N) * i))
        
        # 2-B. 이전 결과들의 사칙연산 조합
        # dp[i] = dp[j] (op) dp[i-j]
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                        
        # 2-C. 정답 확인
        # 현재 사용 횟수(i)로 number를 만들 수 있는지 확인
        if number in dp[i]:
            return i
            
    # 3. 실패 처리
    # 8번까지 사용해도 만들 수 없는 경우
    return -1