from flask import app, Flask, render_template

minha_app = Flask(__name__)

@minha_app.route("/")
def home():
    return render_template("home.html")

@minha_app.route("/artes")
def artes():
    return render_template("Artes.html")

@minha_app.route("/Break-In-Time")
def BIT():
    return render_template("Break_in_Time.html")

@minha_app.route("/Projeto Integrador")
def API():
    return render_template("Projeto_Integrador.html")




if __name__ == '__main__':
    minha_app.run('0.0.0.0')
