from flask import Flask, redirect, url_for
import yugioh

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/deck/<pro>")
def deck(pro):
    card = yugioh.get_card("Mirror Force") #Accepts both name and ID
    if card.type != "Spell Card" and card.type != "Trap Card":
        print(card.name) #Returns "The Wicked Dreadroot"
        print(card.archetype) #Returns "Wicked God"
        print(card.attack) #Returns "4000"
    else:
        print(card.name)
        print(card.description)
    url = "https://static-7.studiobebop.net/ygo_data/card_images/{}.jpg".format(pro.capitalize())
    print (url)
    return "<p>Hello World</p>"
    

'''
@app.route("/yugioh/<card>")
def card(card):
    cardUppercase = card.capitalize()
    url = "https://static-7.studiobebop.net/ygo_data/card_images/{}.jpg".format(cardUppercase)
    print (url)
    return url
'''
'''
@app.route("/view/<card>")
def view(card):
    cardUppercase = card.capitalize()
    cardUrl = "https://static-7.studiobebop.net/ygo_data/card_images/{}.jpg".format(cardUppercase)
    return redirect(cardUrl)
    # return cardUrl 
    # https://static-7.studiobebop.net/ygo_data/card_images/Dark_Magician.jpg
'''