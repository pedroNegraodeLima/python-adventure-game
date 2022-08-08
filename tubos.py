import json
import sys
import os
import random
import time

f = open("content.json", encoding='utf-8')

dContent = json.load(f) 

# Pega o conteúdo do JSON e extrai um ARRAY que, por sua vez, é composto por dicionarios.
content = dContent['texto']
# Para leitura das informaçõs do JSON, a estrutura abaixo deve ser seguida:
# print(content[0]['titulo'])

# Função para escrever (print()) todos os textos do jogo
def LetterPrint(str, delay = 0.05):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')

def logout():
    LetterPrint("Tem certeza que quer sair? Todo o progresso sera perdido.")
    action = input('\n>')
    while action.lower().strip() != "sim":
        if action.lower().strip() == "não":
            # Tem que fazer alguma coisa aqui para que o programa saia dessa função e volte para a função anterior.
            action = ""
        else:
            LetterPrint("As respostas aceitas são: 'não', se quiser continuar com o jogo, ou 'sim', se realmente quiser sair.")
            action = input('\n>')
    LetterPrint("Fim do jogo.")
    sys.exit()

def inicio():
    # Serve como tela inicial
    LetterPrint("\nACORDANDO NUMA FRIA - Working Title")
    LetterPrint("Esse é um jogo no qual cada escolha leva a um resultado diferente. \nPara avançar, basta escrever qual ação deseja fazer em cada momento de escolha.\nCaso queira sair, basta escrever a palavra 'sair' a qualquer momento.")
    LetterPrint("Podemos começar?")
    action = input("\n>")
    while action.lower().strip() != "sim":
        if action.lower().strip() == "não":
            LetterPrint("Até a próxima.")
            sys.exit()
        else:
            LetterPrint("Tente ser mais objetivo na sua resposta.")
            action = input('\n>')

    Tubes()

    # Explica como o joog funciona e como sair do jogo.
    

# cada Função, daqui para baixo, é um ponto de escolha do caminho do jogador. 
# Os pontos de escolha seguintes vão sendo chamados conforme a necessidade. 
# Eles correspondem aos tópicos dentro do arquivo JSON.

def provisorio():
    LetterPrint("\nIsso aqui é o placeholder de um jogo")
    

def Tubes():
    LetterPrint(content[0]['descricao'], 0.05)
    LetterPrint(content[0]['instrucao'])
    while True:
        action = input('\n>')
        if action.lower().strip() == 'usar terminal': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[0]['opção1'])
            TubeRoom()
        elif action.lower().strip() == 'forçar porta': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[0]['opção2'])
            TubeRoom()
        elif action.lower().strip() == 'voltar':
            LetterPrint(content[0]['voltar'])
                        
        elif action.lower().strip() == 'sair':
            LetterPrint(content[0]['sair'])
            logout()
        else:
            LetterPrint(content[0]['else'])   

def TubeRoom():
    LetterPrint(content[1]['descricao'], 0.05)
    LetterPrint(content[1]['instrucao'])
    while True:
        action = input('\n>')
        if action.lower().strip() == 'opção 1': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[1]['opção1'])
            provisorio()
        elif action.lower().strip() == 'opção2': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[1]['opção2'])
            provisorio()
        elif action.lower().strip() == 'olhar': # Opção especial dessa sala.
            LetterPrint(content[1]['olhar'])
            provisorio()
        elif action.lower().strip() == 'voltar':
            LetterPrint(content[1]['voltar'])
            Tubes()
                        
        elif action.lower().strip() == 'sair':
            LetterPrint(content[1]['sair'])
            logout()
        else:
            LetterPrint(content[1]['else'])

def RuinedCor():
    LetterPrint(content[2]['descricao'], 0.05)
    LetterPrint(content[2]['instrucao'])
    while True:
        action = input('\n>')
        if action.lower().strip() == 'opção 1': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[2]['opção1'])
            provisorio()
        elif action.lower().strip() == 'opção2': # Alterar 'opção1' para a paavra que melhor descreve a ação
            LetterPrint(content[2]['opção2'])
            provisorio()
        elif action.lower().strip() == 'voltar':
            LetterPrint(content[2]['voltar'])
                        
        elif action.lower().strip() == 'sair':
            LetterPrint(content[2]['sair'])
            logout()
        else:
            LetterPrint(content[0]['else'])


Tubes()
