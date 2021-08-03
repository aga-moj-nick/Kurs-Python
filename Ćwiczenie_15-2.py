import requests
import json
import webbrowser



params = {
          "limit" : 3,
          "site" : "github",
          "breed" : "american curl"
         }


r = requests.get ("https://api.thecatapi.com/v1/images/search", params)

try:
    cats = r.json ()
except json.decoder.JSONDecoderError:
    print ("Niepoprawny format")
else:
    for picture in cats:
        webbrowser.open_new_tab(picture["url"])
