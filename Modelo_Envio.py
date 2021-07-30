
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "<Digite o assunto do e-mail>"
body = "<Digite o corpo da mensagem>"
sender_email = "<Digite o e-mail destino>"
receiver_email = "<Digite seu e-mail>"
password = "<Digite sua senha>"

# Crie uma mensagem multiparte e defina cabeçalhos
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Adicionando corpo para o e-mail e anexando arquivo
message.attach(MIMEText(body, "plain"))

filename = "<Anexar seu Arquivo>"  # No mesmo diretorio do script

# Abrindo o arquivo em anexo em modo binario
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Codifique o arquivo em caracteres ASCII para enviar por e-mail  
encoders.encode_base64(part)

# Adicionar cabeçalho como par chave / valor à parte do anexo
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Adicionar anexo à mensagem e converter mensagem em string
message.attach(part)
text = message.as_string()

# Faça login no servidor usando contexto seguro e envie e-mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)