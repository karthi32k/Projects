from flask import Flask

app = Flask(__name__)

print(app)


@app.route("/")  # decorator
# functionality of decorator
def hello_world():
    return '<h1 style="text-align: center"> The Batman </h1>' \
           '<p style="color:red"> I am Vengeance!</p>' \
           '<img class="bat"src="https://media.giphy.com/media/YveG2YmL37CbmZVoWB/giphy.gif?cid=ecf05e47mzoubwpypkp1duidqyezco0aeizixulr0114usb5&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="600" height="500">'


# Different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "<b>Good Bye</b>"


# Creating variable paths and converting the path to a specified data type
@app.route("/User/<string:name>/<int:age>/<float:height>")
def greet(name, age, height):
    return (f"Hello {name}!\n "
            f"your age:{age}\n and your height:{height}")


if __name__ == "__main__":
    app.run(debug=True)

# ## Interactive Exerciese
# import time

# current_time = time.time()
# print(current_time)  # seconds since Jan 31st, 1970

# # Write your code below 👇

# def speed_calc_decorator(function):
#     def wreaper_function():
#         start_time = time.time()
#         function()
#         end_time = current_time
#         print(f"{function.__name__} run speed:{end_time - start_time}s")

#     return wreaper_function

# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i

# fast_function()

# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i

# slow_function()
