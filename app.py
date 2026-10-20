from flask import Flask, render_template, request, redirect, url_for
from funcao_grafico_euler import gerar_grafico_euler
from funcao_grafico_ambos import gerar_grafico_ambos
from funcao_grafico_analitico import gerar_grafico_analitico
from flask_sqlalchemy import SQLAlchemy
from banco import *


from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]   =   "sqlite:///banco.db"
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")


    # ==========================================================
    # formularios
    # ==========================================================


@app.route("/form_euler", methods=["GET", "POST"])
def formulario_euler():
    
    if request.method == "POST":
        metodo = "euler"
        beta = float(request.form.get("beta"))
        img = gerar_grafico_euler(beta=beta)

        adicionado = Banco(beta=beta, metodo=metodo, img=img)

        db.session.add(adicionado)
        db.session.commit()
        return redirect(url_for('visualizar_graficos_euler'))

    return render_template("form_euler.html")






@app.route("/form_analitico", methods=['GET','POST'])
def formulario_analitico():
   
    if request.method == "POST":
        metodo = "analitico"
        beta = float(request.form.get("beta"))
        img = gerar_grafico_analitico(beta=beta)

        adicionado = Banco(beta=beta, metodo=metodo, img=img)

        db.session.add(adicionado)
        db.session.commit()
        return redirect(url_for('visualizar_graficos_analitico'))
    return render_template("form_analitico.html")









@app.route('/form_ambos', methods=['GET', 'POST'])
def formulario_ambos():
   
    if request.method == "POST":
        metodo = "ambos"
        beta = float(request.form.get("beta"))
        img = gerar_grafico_ambos(beta=beta)

        adicionado = Banco(beta=beta, metodo=metodo, img=img)

        db.session.add(adicionado)
        db.session.commit()
        return redirect(url_for('visualizar_graficos_ambos'))
    return render_template('form_ambos.html')



    # ==========================================================
    # visualização dos graficos
    # ==========================================================

@app.route('/ver_graficos')
def visualizar_graficos():

    return render_template('ver_graficos.html')

@app.route('/ver_graficos_euler', methods=['POST','GET'])
def visualizar_graficos_euler():
    if request.method == 'POST':
        id = request.form.get('id')
        apagar = db.session.get(Banco, id)

        if apagar:
            db.session.delete(apagar)
            db.session.commit()

    dados = db.session.query(Banco).filter_by(metodo='euler').all()
    return render_template('ver_graficos_euler.html', dados=dados[::-1])

@app.route('/ver_graficos_analitico', methods=['POST','GET'])
def visualizar_graficos_analitico():
    if request.method == 'POST':
        id = request.form.get('id')
        apagar = db.session.get(Banco, id)

        if apagar:
            db.session.delete(apagar)
            db.session.commit()

    dados = db.session.query(Banco).filter_by(metodo='analitico').all()
    return render_template('ver_graficos_analitico.html', dados=dados[::-1])

@app.route('/ver_graficos_ambos', methods=['POST','GET'])
def visualizar_graficos_ambos():
    if request.method == 'POST':
        id = request.form.get('id')
        apagar = db.session.get(Banco, id)

        if apagar:
            db.session.delete(apagar)
            db.session.commit()

    dados = db.session.query(Banco).filter_by(metodo='ambos').all()
    return render_template('ver_graficos_ambos.html', dados=dados[::-1])














@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

