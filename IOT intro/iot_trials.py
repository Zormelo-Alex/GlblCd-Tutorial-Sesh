import requests
class IFTTT_Notification:
    def __init__(self, eventName = "DOM", api_key  = "dyFgePpFpqwJZCjqfzmgtWG7PrYPcIVwQfiQHF4hFA-"):
        self.eventName = eventName
        self.api_key = api_key

    def make_request(self, jsonData = {"Value1": "Alexander", "Value2": "32", "Value3": "new trial"}):
        # create url
        url = f"https://maker.ifttt.com/trigger/{self.eventName}/json/with/key/{self.api_key}"

        try:
            print("sending...")
            response = requests.post(url, jsonData)
            print(response)
            # debug response
            print(response.text)
            print("sent successfully")
        except Exception as e:
            print("run into an error", e)

    