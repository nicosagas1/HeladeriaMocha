from flask import Flask, render_template, request, redirect, url_for, flash
from mail_config import enviar_correo
import os

app = Flask(__name__)
app.secret_key = '7772428b-01cf-4d05-9c3e-cea510398586'

# Ruta para la página de inicio
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para la página de sucursales
@app.route('/sucursales')
def sucursales():
    return render_template('sucursales.html')

# Ruta para la página de promociones
@app.route('/promociones')
def promociones():
    return render_template('promociones.html')

# Ruta para la página de trabaja con mocha
@app.route('/trabajar_en_mocha')
def trabajar_en_mocha():
    return render_template('trabajar_en_mocha.html')

# Ruta para la página de nosotros
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Ruta para la página de pedidos online
@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

# Ruta para el menú, cuando hacen clic en "Ver Menú" en la página de inicio
@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/enviar-cv', methods=['POST'])
def enviar_cv():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_apellido = request.form['nombreApellido']
        email = request.form['email']
        dni = request.form['dni']
        telefono = request.form['telefono']
        
        # Obtener el archivo PDF del CV
        cv_file = request.files['cv']
        
        # Guardar el CV en una carpeta temporal (opcional)
        cv_filename = os.path.join('C:/Users/Usuario/Desktop/HelariaMocha/static/uploads', cv_file.filename)
        cv_file.save(cv_filename)
        
        # Preparar el mensaje del correo
        mensaje = f"Nombre y Apellido: {nombre_apellido}\n"
        mensaje += f"Correo Electrónico: {email}\n"
        mensaje += f"DNI: {dni}\n"
        mensaje += f"Número de Teléfono: {telefono}\n"
        
        # Asunto del correo
        asunto = "¡Ha llegado un currículum!"
        
        # Enviar el correo con el archivo adjunto
        destinatario = "sagasteguinicolas69@gmail.com"
        enviar_correo(destinatario, asunto, mensaje, cv_filename)
        aviso = "Nos ha llegado tu curriculum ✔, ya nos comunicaremos con usted."
        # Redirigir a una página de éxito o de confirmación
        return render_template("trabajar_en_mocha.html", aviso=aviso)

if __name__ == '__main__':
    app.run()
