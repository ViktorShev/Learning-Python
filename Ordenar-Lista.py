# NumList = list(input('Enter numbers: '))
numList = [1,32,65,765,4,32,21,3,5,45,3,4,7,9,984572,1743,876,78,7,5634,234,423,423,7463,7685,4637,345,5]

# selection sort
for j in range(0, len(numList)): 
    majorIndexNumber = j
    for i in range(j, len(numList)):
        if numList[i] < numList[majorIndexNumber]:
            majorIndexNumber = i
    aux = numList[majorIndexNumber]    
    numList[majorIndexNumber] = numList[j]
    numList[j] = aux

print(numList)

numList = [1,32,65,765,4,32,21,3,5,45,3,4,7,9,984572,1743,876,78,7,5634,234,423,423,7463,7685,4637,345,5]

for j in range(0, len(numList)): 
    print(numList)
    for i in range(0, len(numList)):
      if numList[j] > numList[i]:
        aux = numList[j]    
        numList[j] = numList[i]
        numList[i] = aux
        