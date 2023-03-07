
def update_car_info(**cars):
    cars['is_available'] = True
    print(cars)
    return cars


update_car_info(brand='VW', price=15000)
update_car_info(color='red')
print(update_car_info())
