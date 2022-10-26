def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0:
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    if len(answer) == 0:
        return 1
    else:
        return 0