#!/usr/bin/python

import requests
import configparser

config = configparser.ConfigParser()


config.read("../application.ini")

username = config['Main']['username']
url = 'http://192.168.0.9/api/'
url += username

getURL = url + '/lights/1'

response = requests.get(url)
print(response.json())

postURL = url + '/lights/1/state'
json = '{"on":true, "sat":254, "bri":254,"hue":10000}'
requests.put(postURL, json)