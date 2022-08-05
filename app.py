from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    if request.method == 'POST':
        user = request.form['user']
        response = make_response(render_template('cookies.html'))
        response.set_cookie('user_id', user)
        return response

@app.route('/get_cookie')
def get_cookie():
    user = request.cookies.get('user_id')
    return '<h1>Welcome, ' + user + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)