import random



def single_race(N): #N is the number of rolls required to win the race
    
    snails = [0]*13
    
    while max(snails) < N: 
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        
        total = dice_1 + dice_2
        print('dice 1 = ', dice_1,'dice 2 = ', dice_2, '     total: ', total)
        snails[total] += 1
        
    print('\n')
    
    for n in range(1, 13):
        print('Snail ', n, ' scored: ', snails[n])
        
    print('\n')
    print('The winner is: ', snails.index(N))


import random



def race(N):
    
    snails = [0]*13
    
    while max(snails) < N: 
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        
        total = dice_1 + dice_2
        snails[total] += 1
    
    return snails.index(N)

def tournament(N,n):   #N is the number of rolls required to win a race, and n is the number of races
    snail_wins = [0]*13
    for x in range(n):
        Win = race(N)
        snail_wins[Win] += 1
        
    print('\n')
    
    for y in range(1, 13):
        print('Snail ', y, ' won: ', snail_wins[y], 'races.')
