guest = ['Zdzisław Beksiński', 'Adam Savage', 'Viktor Frankl', 'Michio Kaku']
guest.insert(0, 'Barack Obama')
guest.insert(3, 'Bill Nye')
guest.append('Dalai Lama')
guest.sort()

for i in range(len(guest)):
  print(f"Dear {guest[i].title()}, you are cordially invited to our dinner.")


print("The first three items in the list are:", guest[:3])
print("Three items from the middle of the list are:", guest[3:6])
print("The last three items in the list are:", guest[-3:])
