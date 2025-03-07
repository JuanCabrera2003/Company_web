import smtplib, ssl 
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    """Con el metodo getenv podemos acceder a las variables de entorno 
    donde se encuentra nuestra contrasena esto se hace para protegerla"""
    password = os.getenv("PASSWORD")
    
    username = "yesuscabrera2003@gmail.com"

    receiver = "yesuscabrera2003@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)