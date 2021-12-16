import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


def solution_counter(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]


print(solution_counter(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))