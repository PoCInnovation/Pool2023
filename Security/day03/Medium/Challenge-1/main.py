from flask import Flask, render_template
import os
import subprocess as sp

app = Flask(__name__, template_folder='template', static_folder='static')


@app.get('/')
def home():
    out = sp.run(["php", "template/index.php"], stdout=sp.PIPE)
    return out.stdout

@app.route('/F')
def r1():
    return render_template('troll.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4006))
    app.run(debug=True, host='0.0.0.0', port=port)
