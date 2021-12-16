from itertools import permutations
number=[3, 30, 34, 5, 9]
def solution(number): #시간초과..
    arr=list(map(lambda x:''.join(map(str,x)),list(permutations(number))))
    arr.sort(key=lambda x:int(x))
    return arr[len(arr)-1]
print(solution(number))



def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
print(solution(number))

