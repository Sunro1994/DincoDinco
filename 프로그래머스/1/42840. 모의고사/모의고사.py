def solution(answers):
    answer = [0 for _ in range(3)]

    supo1 = [1,2,3,4,5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == supo1[i%len(supo1)]:
            answer[0]+=1
        if answers[i] == supo2[i%len(supo2)]:
            answer[1]+=1
        if answers[i] == supo3[i%len(supo3)] :
            answer[2]+=1
    return [i+1 for i in range(len(answer)) if answer[i] == max(answer)]
