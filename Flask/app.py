from flask import Flask, render_template

app = Flask(__name__)

# Home route + index route
@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")
    # return "the is new text"



if __name__ == "__main__":
    app.run(debug=True)