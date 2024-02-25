rivers = {
    'River Thames': 'England',
    'Tigris River': 'Turkey',
    'Vltava River': 'Czechia'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

for river in rivers:
    print(river)

for country in rivers.values():
    print(country)