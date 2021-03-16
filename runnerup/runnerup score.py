from array import *
n = int(input("number of scores?"))
A = array("l",[])
for i in range(n):
    x = int(input("score"))
    A.append(x)
def runnerup():
    max =0
    for j in range(0,n):
        if max <A[j]:
           max = A[j]
    A.remove(max)
    runerup_score = 0
    for r in range(n-1):
             if runerup_score<A[r]:
                 runerup_score=A[r]
    print(runerup_score)
runnerup()