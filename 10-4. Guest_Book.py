filename = 'guest_book.txt'

while True:
    name = input("Please enter your name (or 'q' to quit): ")
    
    if name == 'q':
        break
    
    print(f"Hello, {name}!")
    
    with open(filename, 'a') as file:
        file.write(name + '\n')