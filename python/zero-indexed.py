A = [5, 2, 1, 6, 3, 7]


def solution(A):
    p1 = 1
    result = float('inf')
    for p2 in range(3, len(A)):
        result = min(result, A[p1] + A[p2])
        if A[p1] > A[p2-1]:
            p1 = p2 - 1
    return result


print(solution(A))
