from random import randrange


legends = ['Wraith', 'Bangalore', 'Mirage', 'Caustic', 'Octane', 'Revenenant', 'Horizon', 'Fuse', 'Gibby', 'Wattson', 'Rampart', 'Loba', 'Lifeline', 'Bloodhound', 'Pathfinder', 'Crypto', 'Valk']
weapons = ['HAVOC', 'Flatline', 'Hemlok', 'R-301', 'Alternator', 'R-99', 'Volt', 'Devotion', 'Spitfire', 'L-STAR', 'G-7', '30-30', 'Bow', 'Charge Rifle', 'Longbow', 'Sentinel', 'EVA-8', 'Mozambique', 'PK', 'Mastiff', 'RE-45', 'P2020', 'Wingman']

def random_legends():
    rand_legends = []
    copy_legends = legends[:]
    for i in range(0,3):
        rand_legend = copy_legends[randrange(0, len(copy_legends))]
        rand_legends.append(rand_legend)
        copy_legends.remove(rand_legend)
    return rand_legends

def random_weapons():
    rand_weapons = []
    copy_weapons = weapons[:]
    for i in range(0,2):
        rand_weapon = copy_weapons[randrange(0, len(copy_weapons))]
        rand_weapons.append(rand_weapon)
        copy_weapons.remove(rand_weapon)
    return rand_weapons


if __name__ == '__main__':
    print('Welcome to the Apex Legends squad and loadout randomizer!')
    print('Press g to generate a random squad and random loadouts or press x to exit the program!')
    while True:
        choice = input('')
        if choice == 'g':
            legend1, legend2, legend3 = random_legends()
            gun1, gun2 = random_weapons()
            print(f'[Farid]\nLegend: {legend1}\nWeapons: {gun1} - {gun2}\n')
            gun1, gun2 = random_weapons()
            print(f'[Adam]\nLegend: {legend2}\nWeapons: {gun1} - {gun2}\n')
            gun1, gun2 = random_weapons()
            print(f'[wrong]\nLegend: {legend3}\nWeapons: {gun1} - {gun2}\n')
        elif choice == 'x':
            print('Exiting program... ')
            break