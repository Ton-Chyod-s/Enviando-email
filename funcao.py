from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import PySimpleGUI as sg
from tqdm import tqdm
import sys
import os

#caminho para os arquivo anexo

def endereco(procurar = True):
    if procurar:
        sg.theme('Reddit')
        local = sg.popup_get_folder(r'Selecione o caminho dos Arquivos')
        caminho = os.chdir(local)
    else:
        pass
    
    return caminho

    
def enviar_email_2(assunto, mensagem, arquivo, para,email,senha):
        txt = [5000]
        for i in tqdm(txt):
            msg = MIMEMultipart()
            msg['Subject'] = assunto
            msg['From'] = email
            msg['To'] = para

            # inicio do email
            msg.preamble = 'Multipart massage.\n'
            msg.attach(MIMEText(mensagem))

            # adicionando anexo
            pdfname = arquivo
            binary_pdf = open(pdfname, 'rb')
            payload = MIMEBase('application', 'octate-stream', Name=pdfname)
            payload.set_payload((binary_pdf).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
            msg.attach(payload)

            # montando email no SMTP server
            smtp = SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email, senha)
            
            # enviar email
            smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        
    
if __name__ == "__main__":
    destinatario = '##@gmail.com'
    senha = '##'
    lista_emails = [
        '##@hotmail.com'
        ]
    assunto_email = 'Teste de email'
    corpo = 'Olá, tudo bem ?\nTeste de envio de e-mail!!'


    for emails in lista_emails:
        endereco()
        enviar_email_2(assunto_email, corpo, 'GERAL-KLAYTON-DIAS.pdf', emails, destinatario, senha)
        
  
