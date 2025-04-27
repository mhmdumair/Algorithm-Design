start = [1,3,0,5,3,5,6,8,8,2,12]
finish = [4,5,6,7,8,9,10,11,12,13,14]

def selectActivity(start,finish):
    n = len(finish)
    i=0
    print(i+1)
    for j in range(n):
        if start[j]>finish[i]:
            print(j+1)
            i=j

selectActivity(start,finish)