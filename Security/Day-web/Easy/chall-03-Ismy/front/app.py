import os
import subprocess as sp

from flask import Flask, make_response, render_template, request

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/', methods =['GET'])
def home():
    return render_template('index.html');

@app.route('/admin/', methods= ['GET'])
def admin():
    login = request.headers.get('Login-Status')
    if (login == 'admin'):
        return render_template('flag.html', flag=os.getenv('FLAG'))
    out = render_template('admin.html')
    return (out, {'Login-Status': 'simple user'})

@app.route('/admin/robots.txt', methods=['GET'])
def robots():
    response = make_response(open('static/robots.txt').read())
    response.headers["Content-type"] = "text/plain"
    return response

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
