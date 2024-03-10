def make_car(manufacturer, model, **kwargs):
    car_info = {'manufacturer': manufacturer, 'model': model}
    car_info.update(kwargs)
    return car_info

car = make_car('Volvo', 'V60', color='Silver', AWD=True),
car2 = make_car('Polestar', 'Polestar 4', color='White', AWD=True),
car3 = make_car('Audi', 'RS3', color='Black', AWD=True),
car4 = make_car('Volkswagen' , 'ID.Buzz', color='White', AWD=False)

print(car,'\n', car2, '\n', car3, '\n', car4)
