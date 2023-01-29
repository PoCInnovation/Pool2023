import os
import subprocess as sp

from flask import Flask, make_response, redirect, request, session

app = Flask(__name__, template_folder='template', static_folder='static')
app.secret_key = "secret_key"

@app.route('/', methods=['GET'])
def home():
    out = sp.run(["php", "template/linktologin.php"], stdout=sp.PIPE)
    return (out.stdout, 302, {'Location': 'index?redirect'})

@app.route('/index')
def login():
    out = sp.run(["php", "template/index.php"], stdout=sp.PIPE)
    return out.stdout

@app.route('/thatoneneither', methods=['GET'])
def crlf():
    args = request.args
    arg1= args.get("username", default="", type=str)
    flag= str(os.getenv("FLAG"))
    out = sp.Popen(["php", "template/login.php", arg1, flag], stdin=sp.PIPE, stdout=sp.PIPE)
    out.stdin.close()
    if "redirected" not in session:
        return "You are not authorized to access this page", 403
    return out.stdout.read().decode('UTF-8')

@app.route('/youwontfuzzthatone')
def miam():
    status = "user"
    page = sp.run(["php", "template/miam.php"], stdout=sp.PIPE)
    out = make_response(page.stdout)
    out.set_cookie('Status', status)
    if (request.cookies.get('Status') == 'admin'):
        session["redirected"] = True
        return redirect("/thatoneneither")
    return out


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)
