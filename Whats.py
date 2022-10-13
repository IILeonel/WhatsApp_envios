#libs que serão usadas:
import pywhatkit as whatsapp  #https://pypi.org/project/pywhatkit/  #https://github.com/Ankit404butfound/PyWhatKit/wiki/Sending-WhatsApp-Messages
import pandas as pd

#Acessando a planilha com os dados dos candidatos:
Contatos = pd.read_excel('Candidatos.xlsx')

#Looping para acessar linha a linha da planilha:
for i, Candidatos in enumerate(Contatos['Nome']):
    nome = Contatos.loc[i,'Nome']
    
    telefone = Contatos.loc[i,'Telefone']
    msg = Contatos.loc[i,'Mensagem']
    
    #formatando o telefone para str:
    tel = str(telefone)
    telCompleto = (f'+55' + tel)

    #concatenando a mensagem de envio:
    msgCompleta = (f'Olá ' + nome +', ' + msg)

    #ação de envio no whats
    whatsapp.sendwhatmsg_instantly(telCompleto,msgCompleta,9,True,7)
    i+=1
    
