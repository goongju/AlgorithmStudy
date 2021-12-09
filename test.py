

def solution(number, k):
    lst=sorted(list(number))
    answer=list(number)
    n=0
    for i in lst:
        while i in answer:
            if n>=k:
                return "".join(answer)
            answer.remove(i)
            n+=1
print(solution("4177252841",4))
