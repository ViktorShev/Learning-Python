from random import randrange


legends = ['Wraith', 'Bangalore', 'Mirage', 'Caustic', 'Octane', 'Revenenant', 'Horizon', 'Fuse', 'Gibby', 'Wattson', 'Rampart', 'Loba', 'Lifeline', 'Bloodhound', 'Pathfinder', 'Crypto', 'Valk']

#def random_squad():
#    random_squad = []
#    stop_value = 0
#    while True:
#        number = randrange(0, 17)
#        legend = legends[number]
#        if legend not in random_squad:
#            random_squad.append(legend)
#            stop_value += 1
#        if stop_value == 3:
#            print(random_squad)
#            break 

def random_squad():
    random_squad = []
    candidates = legends[:]
    for cycle in range(0,3):
        candidate = candidates[randrange(0, len(candidates))]
        random_squad.append(candidate)
        candidates.remove(candidate)  
    print(random_squad)


print('Welcome to the Apex Legends random squad generator!')
print('Press x to exit the program or g to generate a squad of random legends!')

while True:
    choice = input('')
    if choice == 'x':
        print('Exiting program...')
        break
    elif choice == 'g':
        random_squad()
    else:
        break
