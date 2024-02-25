favorite_places = {
    'Caleb': ['Parkway', 'Forest', 'Home'],
    'Ariah': ['Sake Sushi', 'Texas Roadhouse', 'Home'],
    'Rak': ['San Francisco', 'Disney World', 'Uranus'],
    'Alexis': ['Rabbit Trail Alaska', 'Busch Gardens', 'Her Living Room'],
    'Wiynd': ['Grandma\'s Old House in Maine', 'Rocky Mountains', 'Bourbon Grill in Denver'] }

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"{place}")
    print() #added this line to have a blank between statements