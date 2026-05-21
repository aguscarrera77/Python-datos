from flask import Flask, render_template,request

#render template busca dentro de la carpeta templates y lee html.

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template('index.html')

@app.route("/saludar")
def saludar():
    return render_template("saludar.html")

@app.route("/respuesta",methods=['POST'])
def respuesta():
    nombre=request.form["nombre"]
    return render_template("respuesta.html",nombre=nombre)
app.run(debug=True)
