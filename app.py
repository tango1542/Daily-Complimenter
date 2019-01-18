from flask import Flask, render_template, request
import requests
import random


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/compliment',methods=['GET','POST'])
def compliment():
    r = requests.get('https://compliment-api.herokuapp.com/return_data')    #API call
    tempjason = r.json()     #Getting the json object
    compliment_list = (tempjason[0]["compliments"])     #Getting the compliment list portion from the json
    comp_length = len(compliment_list)      #Finding how many items are in the list
    rand_index = random.randint(0,(comp_length-1))      #Getting a random index position of the number of items in the list
    rand_compliment = (tempjason[0]["compliments"][rand_index])     #Using the random index, selecting that index from the list
    print ("This is rand_compliment...  " + rand_compliment)

    picture_list = (tempjason[1]["Pictures"])
    pic_length = len(picture_list)
    rando_index = random.randint(0, (pic_length - 1))
    rand_picture = (tempjason[1]["Pictures"][rando_index])
    print("This is rand_picture...  " + rand_picture)


    return render_template('compliment.html',compliment=rand_compliment,picture=rand_picture)


if __name__ == '__main__':
    app.run(debug=True, port=33507)
