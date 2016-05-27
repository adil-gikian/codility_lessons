def solution(A):
    index = 0
    lengthOfA = len(A)
    while lengthOfA - index >= 3:
        print(index)
        result = checkTriplet(index, index+1, index+2, A)
        if result == True:
            return 1
        else:
            pivot = index + 1
            while lengthOfA - pivot >= 2:
                result = checkTriplet(index, pivot, pivot+1, A)
                if(result == True):
                    return 1
                pivot2 = pivot + 1
                while lengthOfA - pivot2 > 1:
                    result = checkTriplet(index, pivot, pivot2+1, A)
                    if(result == True):
                        return 1
                    pivot2 = pivot2 + 1
                pivot = pivot + 1
        index = index+1
        print(index)
    return 0

def checkTriplet(p, q, r, A):
    print(p , " " , q , " " , r)
    if A[p]+A[q] <= A[r]:
        return False
    elif A[q]+A[r] <= A[p]:
        return False
    elif A[r]+A[p] <= A[q]:
        return False
    else:
        return True
