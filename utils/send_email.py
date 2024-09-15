import requests


def send_email_via_mailgun():
    # Substitua pela sua chave de API do Mailgun
    api_key = '193b65e60846cc239961c2e4384d9993-826eddfb-2f4169a8'
    # Substitua pelo seu domínio do Mailgun
    domain = 'sandbox36a31b91602040b1b9aebbe6f256ea31.mailgun.org'
    url = f'https://api.mailgun.net/v3/{domain}/messages'

    auth = ('api', api_key)
    data = {
        'from': 'postmaster@sandbox36a31b91602040b1b9aebbe6f256ea31.mailgun.org',
        'to': 'julio.jcmarques@gmail.com',  # Substitua pelo e-mail do destinatário
        'subject': 'Hello from Mailgun',
        'text': 'This is a test email sent using Mailgun API.'
    }

    response = requests.post(url, auth=auth, data=data)

    if response.status_code == 200:
        print("Email sent successfully.")
    else:
        print(
            f"Failed to send email: {response.status_code} - {response.text}")


# Chame a função para enviar o e-mail
send_email_via_mailgun()
