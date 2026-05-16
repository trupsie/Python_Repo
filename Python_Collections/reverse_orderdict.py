from collections import OrderedDict
dict = {'new york city': 83837, 'dallas': 33738, 'boston': 37811}
citydata = OrderedDict(dict.items())
print()
print('Below is the city data in normal order:')
for city in citydata:
    print(city, citydata[city])
print()
print('Below is the city data in reverse order:')
for city in reversed(citydata):
    print(city, citydata[city])
print()