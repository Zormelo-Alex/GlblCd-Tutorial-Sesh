from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------
owm = OWM('9feb8ab55ac666276d6eed156cbec7eb')
mgr = owm.weather_manager()

place = input("Please enter a city\n")

place = place.lower()
# Search for current weather in London (Great Britain) and get details
#observation = mgr.weather_at_place('London,GB')
observation = mgr.weather_at_place(place)

w = observation.weather

detailed = w.detailed_status         # 'clouds'
wind = w.wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                # 87
temperature = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
rain = w.rain                    # {}
heat = w.heat_index              # None
clouds = w.clouds 

if(place == "hong kong"):
    print(f"The humidity in {place.upper()} is {humidity}")
elif(place == "tokyo"):
    print(f"The temperature in {place.upper()} is {temperature['temp']} degrees celcius")
else:
    print(f"In {place.upper()} there's, {detailed} \nthe speed of wind is {wind['speed']} \nthe humidity is {humidity} \nthe temperature is {temperature['temp']} degrees celcius \nrain is {rain} \nheat is {heat} \nand cloud is {clouds}")


