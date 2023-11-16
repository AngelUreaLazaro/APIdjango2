from django.core.mail import send_mail
import requests

def enviar_correo_registro(email):
    asunto = 'Registro exitoso'
    mensaje = 'Gracias por registrarte en nuestro sitio web.'
    remitente = 'juangarcia652307@gmail.com'
    destinatario = [email]

    send_mail(asunto, mensaje, remitente, destinatario)

def get_chatgpt_description(product_name):
    chatgpt_api_url = 'https://api.openai.com/v1/chat/completions'
    chatgpt_api_key = 'tu_clave_de_api'

    prompt = f"Describe el componente {product_name}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {chatgpt_api_key}',
    }

    data = {
        'model': 'text-davinci-003',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': prompt}],
    }

    try:
        response = requests.post(chatgpt_api_url, json=data, headers=headers)
        response.raise_for_status()
        description = response.json()['choices'][0]['message']['content']
        return description
    except requests.exceptions.RequestException as e:
        # Manejar errores aquí (puedes loguearlos, levantar una excepción, etc.)
        return f"Error en la llamada a la API: {str(e)}"