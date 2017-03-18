'''
Load the 7 day forecast from DarkSky.Net into Pandas!

In this example you will go back to https://api.darksky.net and use your API key to get the current weather forecast for:
Syrcause, NY (lat=43.0481221, lng=-76.1474244)

In the forecast output, find the daily 7 day forecast (it's the current conditions + 7 days out == 8 days total)

Extract the forecast data and load it into Pandas, then display the Time of the forecast, and high and low temperatures:

HINT: To get the times to show up in a human-readable format, you must convert the DarkSky API time (which is in unix timestamp format) to a Pandas Timestamp date/time format. The pd.to_datetime() function can help you:

time = 1489402800 # this the time format Darksky returns
readable_time = pd.to_datetime(time, unit='s') ## s stands for unix timestamp format
readable_time

Timestamp('2017-03-13 11:00:00')

Just replace the ['time'] column in the DataFrame with the new version.
'''

# TODO: Write Todo list then beneath write your code


# Write code here 
