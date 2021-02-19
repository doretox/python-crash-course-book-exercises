# 6-11. Cities: Make a dictionary called cities. Use the names of three cities
# as keys in your dictionary. Create a dictionary of information about each city
# and include the country that the city is in, its approximate population,
# and one fact about that city. The keys for each city’s dictionary
# should be something like country, population, and fact.
# Print the name of each city and all of theinformation you have stored about it.



cities = {
    'rio de janeiro': {
        'country': 'brazil',
        'population': '6780000000',
        'fact': 'Rio is home to the biggest urban forest in the world',
    },
    'miami': {
        'country': 'united states',
        'population': '470914',
        'fact': 'It’s the only US city that was founded by a woman.',
    },
    'paris': {
        'country': 'france',
        'population': '2175601',
        'fact': 'The Eiffel Tower was supposed to be a temporary installation',
    },
}

for city, city_infos in cities.items():
    country = city_infos['country'].title()
    population = city_infos['population'].title()
    fact = city_infos['fact']

    print(city.title() + " is in " + country + ".")
    print("It has a population of about: " + str(population))
    print("A fun fact about " + country + " is that: " + fact + "." + "\n")