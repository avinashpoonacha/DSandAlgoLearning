
# given a list of elements , find the sum pairs


A = [1,2,3,4,4,6]
sum = 8


# simple in nested loops

def nestedsumpair(Alist,sum):
    for a in range(len(A)):
        for b in range(1,len(A)-1):
            if a+b==sum:
                print(A[a],A[b])
                return


def sortsumpair(Alist,sum):
    Alist.sort()
    (top,bottom)=(0,len(Alist)-1)
    while top < bottom: # need the range bruhh
        if Alist[top]+Alist[bottom] == sum:
            print(Alist[top], Alist[bottom])
            return
        if Alist[top]+Alist[bottom] > sum:
            bottom = bottom -1
        if Alist[top]+Alist[bottom] < sum:
            top = top+1


#sortsumpair(A,sum) # O(nlogn
#nestedsumpair(A,sum) #O(2^n)

def findPairs(A,sum):
    dict={}
    for i,e in enumerate(A):
        if (sum-e) in dict:
            print(A[dict.get(sum-e)],A[i])
        dict[e] = i #storing the index


findPairs(A,sum)