animals = ['tiger', 'lion', 'cheetah']

tiger = "Tigers can use their ears to communicate."
lion = "Lions are the only cats who roar together."
cheetah = "Cheetahs can spot prey up to three miles away."

statements = [tiger, lion, cheetah]

common = ("These three animals belong to the Felidae family, and are "
          "territorial in nature. They mark their territories with scent "
          "to deter intruders and find mates.")

for animal in animals:
    print(animal)

for statement in statements:
    print(statement)

print(common)
