import wbdata

source = wbdata.get_source()
country_info = wbdata.search_countries('united')

print(country_info)