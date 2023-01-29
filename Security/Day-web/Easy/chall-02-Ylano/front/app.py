import os
import subprocess as sp

from flask import Flask, render_template, send_file

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def home():
    out = sp.run(["php", "template/index.php"], stdout=sp.PIPE)
    return out.stdout

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
