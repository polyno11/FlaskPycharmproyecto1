from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def formulariodenota():
    if request.method == "POST":
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if (promedio >= 40 and asistencia >= 75) else 'Reprobado'

        return render_template("ejercicio1.html", promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def nombre():
    if request.method == "POST":
        Nombre1 = str(request.form["Nombre1"])
        Nombre2 = str(request.form["Nombre2"])
        Nombre3 = str(request.form["Nombre3"])
        nombres = [Nombre1, Nombre2, Nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)
        return render_template("ejercicio2.html", nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
    return render_template("ejercicio2.html")

if __name__ == '__main__':
    app.run(port = 8000)