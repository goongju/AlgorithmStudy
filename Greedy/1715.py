#시간초과 뜸
import sys

n=int(input())
cards=sorted([int(sys.stdin.readline()) for i in range(n)])
lst=[cards[0],cards[1]]
for i in range(2,n):
    lst.append(sum(lst))
    lst.append(cards[i])
print(sum(lst))

#==========================================================================

import heapq # 우선순위 큐

N = int(input())

cardList = list(int(input()) for _ in range(N))
heapq.heapify(cardList)
result=0

while len(cardList) != 1:
    num1 = heapq.heappop(cardList)
    num2 = heapq.heappop(cardList)
    Sum = num1 + num2
    result += Sum
    heapq.heappush(cardList,Sum)

print(result)