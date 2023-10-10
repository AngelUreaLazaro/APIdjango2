from django.core.mail import send_mail

def enviar_correo_registro(email):
    asunto = 'Registro exitoso'
    mensaje = 'Gracias por registrarte en nuestro sitio web.'
    remitente = 'juangarcia652307@gmail.com'
    destinatario = [email]

    send_mail(asunto, mensaje, remitente, destinatario)