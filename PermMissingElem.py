def solution(A):
    noOfElem = len(A) + 1
    mylist = []
    counter = 0
    while noOfElem != 0:
       mylist.append(noOfElem)
       noOfElem = noOfElem - 1
       counter = counter + 1
    diff = set(mylist) - set(A)
    return next(iter(diff))
  
  
