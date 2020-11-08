from flask import Flask, render_template, request
app = Flask(__name__)
from TPBase import Verifica,arquivo
from werkzeug.utils import secure_filename
# @app.route("/")
# ,methods=['POST']
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ok")
def index2():
    return render_template('teste.html')

@app.route('/automato',methods=['POST'])
def Automato():
    palavra=request.form.get('palavra')
    resposta,status,transicoes=Verifica(palavra)
    return render_template('index.html',resposta=resposta,status=status,transicoes=transicoes)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('upload/'+ secure_filename(f.filename))
        situacao,status=arquivo(f.filename)
        print(f"E o status do arquivo:{status}")
        return render_template('index.html',situacao=situacao,status=status)
# def hello(name=None):
#     return render_template('index.html', name=name)
