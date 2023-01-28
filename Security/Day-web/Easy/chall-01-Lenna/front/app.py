import os

from flask import Flask, render_template, send_file

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html~')
def backup():
    return send_file("template/index.html~", as_attachment=True)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
