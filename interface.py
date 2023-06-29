import json
import PySimpleGUI as sg
import funcao

def java_script(arquivo):
    with open(arquivo, encoding='utf-8') as meu_json:
        dado = json.load(meu_json)
                
      
class interface:
    def __init__(self):
        #tela inicial 
        sg.theme('Reddit')
        menu_def = ['&Arquivo', ['&Localização']],['&Save',['&Save File']]
        layout_login = [
                    [sg.Menu(menu_def,pad=(10,10))],
                    [sg.Button('Enviar',size=(5,1)), sg.Checkbox('Geral',key='checkbox'),sg.Button('Att',size=(5,1)),sg.Button('Json',size=(5,1))],
                    [sg.Text('Curriculo geral e portifolio',size=(22,1),justification = 'c')],
                    [sg.Text('Destinatário:'), 
                    sg.Text(size=(0,1)),sg.Input(size=(18,1),key='dest',justification = 'l')],
                    [sg.Text('Assunto:     '), sg.Text(size=(0,1)),sg.Input(size=(18,1),key='assunto',justification = 'l')],
                    [sg.Button('Geral',size=(6,1)),sg.Button('Portifolio',size=(8,1)),sg.Button('Remetente',size=(10,1))],
                    ]

        window = sg.Window('E-mail',layout=layout_login, finalize = True)

        def remetente():
            sg.theme('Reddit')
            remetente_layout = [
                [sg.Button('Voltar',size=(5,1)), sg.Text('Remetente',size=(15,1),justification = 'c'),sg.Button('Att',size=(5,1)),sg.Button('Json',size=(5,1))],
                [sg.Text('E-mail:\t'), sg.Text(size=(0,1)),sg.Input(size=(18,1),key='email',justification = 'l')],
                [sg.Text('Senha:\t'), sg.Text(size=(0,1)),sg.Input(size=(18,1),key='senha',justification = 'l')],
            ]
            
            window = sg.Window('E-mail',layout=remetente_layout, finalize = True)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                
                if event == 'Voltar':
                    window.close()
                    programa = interface()
                    programa
                    
                    
                if event == 'Att' :
                    dados = {
                        "email": values['email'],
                        "senha": values['senha']
                    }
                    with open("remetente.json", 'w') as file:
                        json.dump(dados, file, indent=4)
                        
                if event == 'Json':
                        f = open('remetente.json') 
                        data = json.load(f)                       
                        s = json.dumps(data, indent=2)
                        
                        def chr_remove(old, to_remove):
                            new_string = old
                            for x in to_remove:
                                new_string = new_string.replace(x, '')
                            return new_string
                        
                        arquivo = chr_remove(s, '$({},"')
                        sg.popup_quick_message(arquivo)
                                
            window.close()

        def geral():
            sg.theme('Reddit')
            geral_layout = [
                [sg.Button('Voltar',size=(5,1)), sg.Text('Corpo da mensagem',size=(15,1),justification = 'c'),sg.Button('Att',size=(5,1)),sg.Button('Json',size=(5,1))],
                [sg.Multiline(size=(42,10),key='mensagem',justification = 'l',do_not_clear=False)]
            ]
            
            window = sg.Window('E-mail',layout=geral_layout, finalize = True)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                
                if event == 'Voltar':
                    window.close()
                    programa = interface()
                    programa
                    
                #atualizar informações de mensagem
                if event == 'Att':
                    fileName = "geral.json"
                    jsonObject = {
                        "corpo_mensagem": values['mensagem'],
                        
                    }

                    file = open(fileName, "w")
                    json.dump(jsonObject, file, sort_keys=True, indent=4)
                    file.close()
                    
                if event == 'Json':
                        f = open('geral.json') 
                        data = json.load(f)                       
                        s = json.dumps(data, indent=2)
                        
                        def chr_remove(old, to_remove):
                            new_string = old
                            for x in to_remove:
                                new_string = new_string.replace(x, '')
                            return new_string
                        
                        arquivo = chr_remove(s, '$({},"')
                        sg.popup_quick_message(arquivo)
                            
            window.close()
        
        def portifolio():
                sg.theme('Reddit')
                portifolio_layout = [
                    [sg.Button('Voltar',size=(5,1)), sg.Text('Corpo da mensagem',size=(15,1),justification = 'c'),sg.Button('Att',size=(5,1)),sg.Button('Json',size=(5,1))],
                    [sg.Multiline(size=(42,10),key='mensagem',justification = 'l',do_not_clear=False)]
                ]
                
                window = sg.Window('E-mail',layout=portifolio_layout, finalize = True)
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        break
                    
                    if event == 'Json':
                        f = open('portifolio.json') 
                        data = json.load(f)                       
                        s = json.dumps(data, indent=2)
                        
                        def chr_remove(old, to_remove):
                            new_string = old
                            for x in to_remove:
                                new_string = new_string.replace(x, '')
                            return new_string
                        
                        arquivo = chr_remove(s, '$({},"')
                        sg.popup_quick_message(arquivo)
                        
                    if event == 'Voltar':
                        window.close()
                        programa = interface()
                        programa
                        
                    #atualizar informações de mensagem
                    if event == 'Att':
                        fileName = "portifolio.json"
                        jsonObject = {
                            "corpo_mensagem": values['mensagem'],
                            
                        }

                        file = open(fileName, "w")
                        json.dump(jsonObject, file, sort_keys=True, indent=4)
                        file.close()
                        
                   
                window.close()
        
        while True:
            event, values = window.read()    
            if event == sg.WIN_CLOSED:
                break
            
            #atualizar informações de destinatário
            if event == 'Att':
                fileName = "destinatario.json"
                jsonObject = {
                    "Destinatario": values['dest'],
                    "assunto": values['assunto'],
                }

                file = open(fileName, "w")
                json.dump(jsonObject, file, sort_keys=True, indent=4)
                file.close()
                
            if event == 'Json':
                f = open('destinatario.json') 
                data = json.load(f)                       
                s = json.dumps(data, indent=2)
                
                def chr_remove(old, to_remove):
                    new_string = old
                    for x in to_remove:
                        new_string = new_string.replace(x, '')
                    return new_string
                
                arquivo = chr_remove(s, '$({},"')
                sg.popup_quick_message(arquivo)
                 
            try:    
                #enviar o email com as informações
                if event == 'Enviar':
                    with open("destinatario.json", encoding='utf-8') as meu_json:
                        dado = json.load(meu_json)
                    with open("remetente.json", encoding='utf-8') as meu_json:
                        dado1 = json.load(meu_json)   
                    with open("geral.json", encoding='utf-8') as meu_json:
                        dado2 = json.load(meu_json)  
                    with open("portifolio.json", encoding='utf-8') as meu_json:
                        dado3 = json.load(meu_json)  
                        
                    remetente_ = dado1['email']
                    senha = dado1['senha']
                    destinatario = dado['Destinatario']
                    assunto_email = dado['assunto']
                    
                    if values['checkbox']: 
                        corpo = dado2['corpo_mensagem']       
                        funcao.enviar_email_2(assunto_email, corpo, 'GERAL-KLAYTON-DIAS.pdf', destinatario, remetente_, senha)
                                            
                    else:
                        corpo = dado3['corpo_mensagem']   
                        funcao.enviar_email_2(assunto_email, corpo, 'KLAYTON-DIAS-portfolio.pdf', destinatario, remetente_, senha)
            
                    sg.popup_no_buttons('E-mail enviado com susseso', keep_on_top=True)
            
            except :
                sg.popup_no_buttons('Erro ao enviar e-mail\n\n''Possiveis erros:\n''- Conferir arquivos .json\n''- Conferir arquivos .pdf', keep_on_top=True)
                
            if event == 'Geral':
                window.close()
                geral()
            
            if event == 'Portifolio':
                window.close()
                portifolio()
                
            if event == 'Remetente':
                window.close()
                remetente()  
            try:    
                if event == 'Localização':
                    funcao.endereco()     
            
            except :
                pass    
                 
        window.close()
        
    
if __name__ == '__main__':
    programa = interface()
    programa
    

