from flask import Flask, redirect, url_for
import csv
import yugioh

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/deck/<card>")
def deck(card):
    card2 = yugioh.get_card("Mirror Force") #Accepts both name and ID
    if card2.type != "Spell Card" and card2.type != "Trap Card":
        print(card2.name) #Returns "The Wicked Dreadroot"
        print(card2.archetype) #Returns "Wicked God"
        print(card2.attack) #Returns "4000"
    else:
        print(card2.name)
        print(card2.description)
    url = "https://static-7.studiobebop.net/ygo_data/card_images/{}.jpg".format(card.capitalize())
    print (url)
    return "<p>Hello World</p>"
    
