import requests

eventName = "DOM"
api_key = "dyFgePpFpqwJZCjqfzmgtWG7PrYPcIVwQfiQHF4hFA-"

# create url
url = f"https://maker.ifttt.com/trigger/{eventName}/json/with/key/{api_key}"

jsonData = {
    "Value1": "Alexander",
    "Value2": "32",
    "Value3": "fifteen"
}


try:
    response = requests.post(url, jsonData)
    print(response)
    # debug response
    print(response.text)
except:
    print("run into an error")