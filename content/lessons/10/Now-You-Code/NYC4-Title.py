'''
Now You Code 4: Syracuse Weather

Write a program to load the Syracuse weather data from Dec 2015 in
JSON format into a Python list of dictionary. The file is:

"NYC4-syr-weather-dec-2015.json"

After you load this data calculate the number of days where the
'Mean TemperatureF' is above freezing ( > 32 degrees)

Store the days above freezing and below freezing into a dictionary
and then print out the dictionary like this:

{'below-freezing': 4, 'above-freezing': 27}

'''

# TODO: Write Todo list then beneath write your code


# Write code here

import json

with open('NYC4-syr-weather-dec-2015.json', encoding='utf8') as f:
    weather = json.loads(f.read())

stats =  { 'above-freezing' : 0, 'below-freezing' : 0 }
for w in weather:
    if w['Mean TemperatureF'] > 32:
        stats['above-freezing'] +=1
    else:
        stats['below-freezing'] +=1
        
print(stats)
