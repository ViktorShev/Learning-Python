arr = [1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1]

def contar(arr):
    islands = 0
    arr.insert(0, 0)                                   
    for i in range(len(arr)):
        if arr[i-1] == 0 and arr[i] == 1:
            islands += 1

    return islands
    

print(contar(arr))