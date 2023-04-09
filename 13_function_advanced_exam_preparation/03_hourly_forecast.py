def forecast(*args):
    register = {'Sunny': [],
                'Cloudy': [],
                'Rainy': [],
                }

    def sort_by_weather(argument):
        nonlocal register
        for location, weather in args:
            if weather == argument:
                register[weather].append(location)

    sort_by_weather('Sunny')
    sort_by_weather('Cloudy')
    sort_by_weather('Rainy')

    [city_list.sort() for city_list in register.values()]
    result = []

    for weather, cities in register.items():
        for city in cities:
            string = f"{city} - {weather}"
            result.append(string)

    return '\n'.join(result)