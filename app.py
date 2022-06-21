

from flask import Flask , render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Pessoa(db.Model):

    __tablename__= 'pessoa'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    dia = db.Column(db.String)
    jornada = db.Column(db.String)
    hora = db.Column(db.String)

    def __init__(self, nome, dia, jornada, hora):
        self.nome = nome
        self.dia = dia
        self.jornada = jornada
        self.hora = hora

db.create_all()


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/registrar")    
def registrar():
    return render_template("registro.html")

@app.route("/registro", methods=['GET', 'POST'])  
def registro():
    if request.method == "POST":
        nome = request.form.get("nome") 
        dia = request.form.get("dia") 
        jornada = request.form.get("jornada") 
        hora = request.form.get("hora") 

        if nome and dia and jornada and hora:
            p = Pessoa(nome, dia, jornada, hora)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("index")) 

@app.route("/lista")  
def lista():
    pessoas = Pessoa.query.all()
    return render_template("lista.html",pessoas=pessoas)




if __name__ == '__main__':
    app.run(debug=False)    