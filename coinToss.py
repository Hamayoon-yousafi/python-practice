import random

def coin_flip(): 
    coin_sides = ['heads', 'tails']
    random_side = coin_sides[random.randint(0,1)]
    return random_side

print(f"it's {coin_flip()}")