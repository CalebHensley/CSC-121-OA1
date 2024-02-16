import random

def shoot():
    alien_colors = ['green', 'yellow', 'red']
    hit = random.choice(alien_colors)
    
    if hit == 'green':
        print("You hit green and earned 5 points")
    elif hit == 'yellow':
        print("You hit yellow and earned 10 points")
    elif hit =='red':
        print("You hit red and earned 15 points")

shoot()