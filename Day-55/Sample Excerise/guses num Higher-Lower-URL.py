from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1 style='text-align:center'> Guess a number between 0 and 9 </h1>" \
           '<iframe src="https://giphy.com/embed/VxHslc0YBJqAXGaaZ7" width="480" height="329" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe>'


@app.route("/<int:guess>")
def random_num(guess):
    if guess > random_number:
        return "<h1 style='color:red'> This number is too high, Try again </h1>"\
               "<img src='https://media.giphy.com/media/cuacpVsdEla1xO2T72/giphy.gif?cid=ecf05e47tvnwub90vgm1qbzbfv2dnnp6zoqbvp0o1j6hnsvh&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

    elif guess < random_number:
        return "<h1 style='color:blue'> This number is too low, Try again </h1>"\
               "<img src='https://media.giphy.com/media/Sid4QgwDxJ8l2/giphy.gif?cid=790b7611je7ghoqhdiyhpkp1gx0or26yvwbw0wx5oztvpfyu&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"\


    else:
        return "<h1 style='color:green'> You've figured it out! </h1>"\
               "<img src='https://media.giphy.com/media/V6EF7xqSAsUz2AvEfK/giphy.gif?cid=ecf05e47wi125ks1a4buqlcecx73xz0r6skw3zx0jryr1fpx&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)
