def partition(A, p, r):
    q = j = p
    while j < r:
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[r] = A[r], A[q]
    return q

A = [86, 66, 21, 68, 88, 94, 42, 96, 73, 72]
partition(A, 0, len(A)-1)
print(A)