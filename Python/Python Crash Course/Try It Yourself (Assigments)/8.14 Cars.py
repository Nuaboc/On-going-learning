def car_info(manufacturer, model, **specs):
    # esta funcion tiene 2 parametros posicionales y uno arbitrario para insertar x cantidad de info
    car_details = {}
    car_details['brand'] = manufacturer
    car_details['modelo'] = model
    for key, value in specs.items():
        car_details[key] = value
    return car_details


car = car_info('mazda', 'rx-8', color='red',
                liters='1.3', year='2004',
                 price='30,000', owner='me')

print(car)
