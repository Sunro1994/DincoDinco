def solution(numLog):
    command = { 1 : "w" , -1: "s" , 10 : "d",  -10 : "a"}
    answer = []
    for i in range(len(numLog)-1):
        answer.append(command[numLog[i+1] - numLog[i]])

    return "".join(answer)