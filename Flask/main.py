from flask import Flask , render_template

m = Flask(__name__)
@m.route('/')
def ret():
    return "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"


if __name__ == "__main__":
    m.run(debug=True)