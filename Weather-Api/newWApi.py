from pprint import pprint
import requests
APIKEY = "9feb8ab55ac666276d6eed156cbec7eb"

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={APIKEY}')
pprint(r.json)