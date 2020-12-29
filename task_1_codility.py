# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def increment_helper(a, b):
    if a == b:
        return a
    else:
        a+=1
        return a
        
def solution(A):
    # write your code in Python 3.6
    A.sort()
    idx = A[0]
    last = A[-1]
    for num in A:
        idx = increment_helper(idx, num)
        if num < 0 and num == last:
            return 1
        if idx == last:
            idx+=1
            break
        if num < 0:
            continue
        if idx == num:
            continue
    return idx

# print(solution([1,1,2,3,4,6]))
# print(solution([1,3,6,4,1,2]))
# print(solution([1,2,3]))
# print(solution([-1,-3]))
# print(solution([6,6,6,6]))