from flask import Flask, render_template, request
app = Flask(__name__)
from TPBase import Verifica
# @app.route("/")
# ,methods=['POST']
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/automato',methods=['POST'])
def Automato():
    palavra=request.form.get('palavra')
    resposta,status=Verifica(palavra)
    return render_template('index.html',resposta=resposta,status=status)
# def hello(name=None):
#     return render_template('index.html', name=name)
