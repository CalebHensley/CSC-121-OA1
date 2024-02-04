import random

cars = ['Volvo V60', 'Volvo V90', 'Polestar 1', 'Polestar 4']
car = random.choice(cars)
message = f"One day I hope to own a {car}"
print(message)

for i in range(len(cars)):
  print(f"One day I hope to own a {cars[i].title()}")