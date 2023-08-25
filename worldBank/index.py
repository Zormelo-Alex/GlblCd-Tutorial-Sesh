import wbdata

source = wbdata.get_source()

country = input("Please enter the country\n")

country_info = wbdata.search_countries(country)

indicator = wbdata.get_indicator(source=1)

def getCode():
    for i in country_info:
        return i['id']

code = getCode()

country_name = ''

for i in indicator:
    country_details = wbdata.get_data(i['id'], country = code)
    date = country_details[0]['date']

    for j in country_details:
        print(f"{j} \n\n")
    
# for j in country_details:
#     # print(j)
#     country_name = j['country']['value']

# print(country_name)
# print(date)
# print(indicator)