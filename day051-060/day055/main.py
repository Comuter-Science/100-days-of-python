from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)

# def make_bold(function):
#     def f():
#         return f"<b>{function()}</b>"
#     return f


# def make_emphasis(function):
#     def f():
#         return f"<em>{function()}</em>"
#     return f


# def make_underlined(function):
#     def f():
#         return f"<u>{function()}</u>"
#     return f


def img(src):
    return f'<img style="display: block;" src="{src}" />'


@app.route('/')
def index():
    return '<h1>Guess a number between 0 and 9</h1>' + img("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")


@app.route('/<int:number>')
def guess(number):
    if number > random_number:
        return '<h1>Too high, try again!</h1>' + img('https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif')
    elif number < random_number:
        return '<h1>Too low, try again!</h1>' + img('https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif')
    else:
        return '<h1>You found me!</h1>' + img('https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif')


if __name__ == '__main__':
    app.run(debug=True)
