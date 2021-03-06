#!/usr/bin/env python3
#-*- coding: utf-8 -*- 
import urllib.request, json
#import weatherconfig
#import weatherconf




city = "Helsinki"
api_key = "f01a5b8199fe4ec8b811d775b6bb0e9b"

weather = eval(str(urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(city, api_key)).read())[2:-1])

currWeather = weather['weather'][0]

main = currWeather['main']
description = currWeather['description']

icon = ''

if main == 'Drizzle':
  icon = ''
elif main == 'Rain':
  icon = ''
elif main == 'Thunderstorm':
  icon = ''
elif main == 'Snow':
  icon = ''
elif main == 'Clear':
  icon = ''
elif main == 'Clouds':
  icon = ''

info = description.capitalize()
temp = int(float(weather['main']['temp']) - 272.15)

print('%s %s, %i °C' % (icon, main, temp))
