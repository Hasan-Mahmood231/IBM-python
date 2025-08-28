# from flask import Flask , render_template , request

# app = Flask(__name__)

# @app.route('/form',methods = ['GET','POST'])
# def form():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f'Hellow dear {name}'
    
#     return render_template('form.html')
    
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']   # get the submitted name
        return f"Hello {name}"        # 👈 return this directly to browser
    
    # if it's just GET request, show the form
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)


