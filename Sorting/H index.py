def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
print(solution(	[0, 1, 0, 9, 1, 4, 7, 2, 3, 4, 2]))

arr=[0, 1, 0, 9, 1, 4, 7, 2, 3, 4, 2]
print(sorted(arr))
