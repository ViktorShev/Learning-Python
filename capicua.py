word = input('Ingerese una palabra: ')

#def capicua(word):
#    is_capicua = False
#    right_left = ''
#    for i in reversed(range(len(word))):
#        right_left += word[i]
#    if right_left == word:
#        is_capicua = True
#    
#    return f'Es capicua? {is_capicua}'
#
#print(capicua(word))

def capicua (word):
    is_capicua = False
    index = 0
    for i in reversed(range(len(word))):
        if word[index] == word[i]:
            index += 1
            is_capicua = True
            continue
        elif word[index] != word[i]:
            is_capicua = False
            break
    return is_capicua
        
print(capicua(word))