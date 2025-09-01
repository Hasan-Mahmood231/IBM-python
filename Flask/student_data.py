from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('student_data.html',
                           name = 'hassan',
                           is_topper = True,
                           subject = ['math','physics','english']
                           )

if __name__ == '__main__':
    app.run(debug=True)
