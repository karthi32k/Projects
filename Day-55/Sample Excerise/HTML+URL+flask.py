from flask import Flask

app = Flask(__name__)

print(app)


@app.route("/")  # decorator
# functionality of decorator
def hello_world():
    return '<h1 style="text-align: center"> The Batman </h1>' \
           '<p style="color:red"; "text_again:center"> I am Vengeance!</p>' \
           '<img class="bat"src="https://media.giphy.com/media/YveG2YmL37CbmZVoWB/giphy.gif?cid=ecf05e47mzoubwpypkp1duidqyezco0aeizixulr0114usb5&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="600" height="500">'


def make_bold(function):
    def wrapper_function():
        text = function()
        return "<b>" + text + "</b>"

    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}</u>"

    return wrapper_function


# Different routes using the app.route decorator

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return ("You have given them everything\n "
            "Not Everything Not Yet")


@app.route("/bye/bat")
def intro():
    return "<b>They think i'm hiding in the shadow, but I AM THE SHADOW</b>"


if __name__ == "__main__":
    app.run(debug=True)