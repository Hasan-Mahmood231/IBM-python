from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def login_home():
    name = request.form['username']
    password = request.form['password']
    
    user = {
        'hassan':'222',
        'shahid': '22',
        'sanana': '123'
    }

    if name in user and password == user[name]:
        return f'{name}, your response has been submitted successfully.'
    else:
        error_message = "Wrong username or password. Please try again."
        return render_template('/form.html', error=error_message)

    # For demo, just returning a success message
    

if __name__ == '__main__':
    app.run(debug=True)




    # valuid_user = {
    #     'hassan' : '123',
    #     'saim':'321',
    #     'jalal':'1234'
    # }
    # if username in valuid_user & password == valuid_user[username]:
    #     # redirect(url_for('form'))
    #     pass
    # else:
    #     return 'invaluid cradentials'


# @app.route('/about', methods = ["GET","POST"])
# def about():
#     return "about page content"

# @app.route('/contact', methods = ["GET","POST"])
# def contact():
#     return "contact page content"


# if __name__ == "__main__":
#     app.run(debug=True)