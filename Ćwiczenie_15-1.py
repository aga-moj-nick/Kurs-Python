import requests
import json
import webbrowser
from pprint import pprint


użytkownik = ""
def req (adres, params):
    return requests.get(adres, params)

while użytkownik.upper () != "W":
    użytkownik = input ("Wybierz: K, jeśli chcesz przeczytać o kotach, P, jeśli chcesz przeczytać o psach, W, jeśli chcesz wyjść: ")

    if użytkownik.upper () == "W":
        break
    elif użytkownik.upper () == "K":
        zwierzę = "https://cat-fact.herokuapp.com/facts/random/"
    elif użytkownik.upper () == "P":
        zwierzę = "https://cat-fact.herokuapp.com/facts/random/"
    else:
        print ("Nie ma takiej literki")


    params = {
              "amount" : 10,
              "pies_lub_kot" : "kot",
              "pies_lub_kot" : "pies"
              }

    
    try:
        pies_lub_kot = req(zwierzę, params).json ()
    except json.decoder.JSONDecoderError:
        print ("Niepoprawny format")
    else:
        for kot in pies_lub_kot:
            print (kot ["text"])
        for pies in pies_lub_kot:
            print(pies ["text"])



