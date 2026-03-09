from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    
    return True
            

def solution(numbers):
    tot = 0
    answer = set()
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers,i)
        for p in perm:
            answer.add(int(''.join(p)))
    
    for i in answer:
        if is_prime(i):
            tot +=1
    return tot