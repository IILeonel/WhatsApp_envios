# Envios automatico de mensagens via WhatsApp

Script Python que possibilita o envio de mensagens via WhatsApp Web com o numero, nome e a mensagem desejada. Pode ser utilizado para contatos em massa, seja na area de Publicidade ou até mesmo Recursos Humanos. O Script lê os dados de uma planilha Excel que o usuario deverá passar os dados antes (Nome, numero e mensagem).

# Detalhes
* O Script envia mensagens para numeros salvos em sua agenda ou numeros não salvos.
* O WhatsApp ja deve estar conectado via QR code antes de rodar o script.
* Voce deverá passar o DDD em todos os numeros ao adiciona-lo na planilha Excel.
* A lib pyinstaller foi utilizada apenas para gerar um arquivo executavel.

# Requesitos
* Python 3.8: Download em https://www.python.org/downloads
* Pandas: Comando pip install pandas
* Pywhatkit: Comando pip install pywhatkit
* Odfpy: Comando pip install odfpy
* OpenpyXl: Comando pip install OpenpyXl
* Pyinstaller: Comando pip install pyinstaller
