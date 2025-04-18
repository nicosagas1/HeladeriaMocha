import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
load_dotenv()

def enviar_correo(destinatario, asunto, mensaje, archivo_curriculum):
    # Configuración del servidor SMTP de Gmail
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    correo_origen = os.getenv('CORREO_ORIGEN')  # Correo de origen
    contraseña = os.getenv('CONTRASENA')  # Contraseña de aplicación

    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = correo_origen
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    # Adjuntar el archivo del CV
    if archivo_curriculum:
        try:
            with open(archivo_curriculum, 'rb') as archivo_adj:
                parte_adjunta = MIMEBase('application', 'octet-stream')
                parte_adjunta.set_payload(archivo_adj.read())
                encoders.encode_base64(parte_adjunta)
                parte_adjunta.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_curriculum)}')
                msg.attach(parte_adjunta)
        except Exception as e:
            print(f"Error al adjuntar el archivo: {e}")

    try:
        # Conectarse al servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()  # Iniciar conexión segura
        servidor.login(correo_origen, contraseña)  # Iniciar sesión

        # Enviar el correo
        servidor.sendmail(correo_origen, destinatario, msg.as_string())
        print(f"Correo enviado a {destinatario} con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        servidor.quit()  # Cerrar conexión
