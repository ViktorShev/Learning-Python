arr2 = [1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1]

def contar(arr):
    islands = 0
    new_arr = arr.insert(0, 0)                                   
    for i in range(1, len(new_arr)):
        if new_arr[i-1] == 0 and new_arr[i] == 1:
            islands += 1

    return islands
    
def contar2(arr):
    islands = 0
    previousState = 0
    for i in range(len(arr)):
        if previousState == 0 and arr[i] == 1:
          islands += 1
        previousState =  arr[i]

    return islands


print(contar2(arr2))
print(contar(arr2))