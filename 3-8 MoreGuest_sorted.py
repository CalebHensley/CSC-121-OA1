guest = ['Zdzisław Beksiński', 'Adam Savage', 'Viktor Frankl', 'Michio Kaku']
guest.insert(0, 'Barack Obama')
guest.insert(3, 'Bill Nye')
guest.append('Dalai Lama')
guest.sort()

for i in range(len(guest)):
  print(f"Dear {guest[i].title()}, you are cordially invited to our dinner.")
