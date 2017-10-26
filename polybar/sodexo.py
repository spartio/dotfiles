#!/usr/bin/env python3
#-*- coding: utf-8 -*- 
import urllib.request, json


url = 'https://api.spotify.com/v1/search?type=artist&q=snoop'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))