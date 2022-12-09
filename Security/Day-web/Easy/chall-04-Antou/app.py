import os
import subprocess as sp

from flask import Flask

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def home():
    out = sp.run(["php", "template/index.php"], stdout=sp.PIPE)
    return (out.stdout, 302, {'Location': 'login.php?redirect'})

@app.route('/login.php')
def login():
    out = sp.run(["php", "template/login.php"], stdout=sp.PIPE)
    return out

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4004))
    app.run(debug=True, host='0.0.0.0', port=port)
