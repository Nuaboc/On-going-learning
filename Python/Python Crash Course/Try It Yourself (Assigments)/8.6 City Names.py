# 8.6 city names

def city_country(city, country):
    # aqui utilizare return
    lugares = city + ', ' + country + "."
    return lugares.title()

places = city_country('Bayamon', 'Puerto Rico')
# no es necesario esta variable

print (places)

print (city_country('Ponce', 'puerto rico'))

print (city_country('tokio', 'japan'))
