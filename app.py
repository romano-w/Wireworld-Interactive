######################################################################
# Author: Will Romano
# username: romanow

# Assignment: Final Project
# Purpose: Implement Wireworld cell automation as a Python based web app

######################################################################

import time
from Matrix import *
from flask import Flask, request, send_from_directory
import datetime

app = Flask(__name__, static_url_path="")


@app.route("/")
def homepage():
    return app.send_static_file("index.html")

# @app.route("/")
# def homepage():
#     the_time = datetime.time().strftime("%A, %d %b %Y %l:%M %p")
#
#     html = render_template('homepage.html', time=the_time)
#     return html

# @app.route('/')
# def render_static(page_name):
#     return render_template('%s.html' % page_name)


# @app.route("/")
# def homepage():
#     the_time = datetime.time().strftime("%A, %d %b %Y %l:%M %p")
#
#     return """
#     <h1>Hello heroku</h1>
#     <p>It is currently {time}.</p>
#
#     <img src="http://loremflickr.com/600/400">
#     """.format(time=the_time)


def main():
    """
    TODO:Add docstring
    :return: None
    """
    matrix = Matrix(30, 15)

    # Top half of timer
    matrix.matrix[6][10], matrix.matrix[6][11], matrix.matrix[6][12], matrix.matrix[6][13], matrix.matrix[6][14], matrix.matrix[6][15] = 2, 3, 3, 3, 3, 3
    # Bottom half of timer
    matrix.matrix[8][10], matrix.matrix[8][11], matrix.matrix[8][12], matrix.matrix[8][13], matrix.matrix[8][14], matrix.matrix[8][15] = 3, 3, 3, 3, 3, 2
    # Ends of timer
    matrix.matrix[7][9], matrix.matrix[7][16] = 1, 1
    # Wire leading out
    matrix.matrix[7][17], matrix.matrix[7][18], matrix.matrix[7][19], matrix.matrix[7][20], matrix.matrix[7][21], matrix.matrix[7][22] = 3, 3, 3, 3, 3, 3
    matrix.matrix[7][23], matrix.matrix[7][24], matrix.matrix[7][25], matrix.matrix[7][26], matrix.matrix[7][27], matrix.matrix[7][28], matrix.matrix[7][29] = 3, 3, 3, 3, 3, 3, 3

    while True:
        matrix.term_display()
        time.sleep(.4)
        matrix.generation_progress()


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
