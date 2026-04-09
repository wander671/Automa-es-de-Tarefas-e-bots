# bibliotecas = pacotes de códigos prontos para serem usados
# pip install pyautogui

import pyautogui # biblioteca para automação de tarefas no computador (mouse e teclado)
import time # biblioteca para trabalhar com tempo (pausas, horários, etc)

# pyautogui.click -> clicar em um local da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla
# pyautogui.hotkey -> aperta um atalho de teclado (hotkey)
pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando (1 segundo)
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login' # link do site da empresa
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
pyautogui.press('win') # escreveria o nome do navegador
pyautogui.write('chrome') # apertaria enter para abrir o navegador
pyautogui.press('enter') # escreveria o link do site

pyautogui.write(link)
pyautogui.press('enter')
# fazer uma pausa maior pro site carregar
time.sleep(3) # tempo de espera em segundos 

# Passo 2: fazer login
# clicar no campo de email
pyautogui.click(x=538, y=557) # coordenadas do campo de email
pyautogui.write('wanderfarias72@gmail.com') # escrever o email
pyautogui.press('tab') # apertar tab para ir para o campo de senha
pyautogui.write('Sua senha muito muito dificilima') # escrever a senha
pyautogui.press('tab') # apertar tab para ir para o botão de login
pyautogui.press('enter') # apertar enter para fazer login
# fazer uma pausa maior pro site carregar
time.sleep(4) # tempo de espera em segundos

# Passo 3: Abrir a base de dados (importa o aqurivo)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv('Produtos.csv') # ler a tabela de produtos
print(tabela) # mostrar a tabela no terminal 


for linha in tabela.index: # para cada linha da tabela
    # Passo 4: Cadastra 1 produto
    #código
    pyautogui.click(x=524, y=386) # clicar no campo do código
    codigo = str(tabela.loc[linha, 'codigo']) # pegar o código do produto da tabela
    pyautogui.write(codigo) # escrever o código do produto
    pyautogui.press('tab') # apertar tab para ir para o campo da marca

    # marca
    marca = str(tabela.loc[linha, 'marca']) # pegar a marca do produto da tabela
    pyautogui.write(marca) # escrever a marca do produto
    pyautogui.press('tab') # apertar tab para ir para o campo do tipo

    # tipo
    tipo = str(tabela.loc[linha, 'tipo']) # pegar o tipo do produto da tabela
    pyautogui.write(tipo) # escrever o tipo do produto
    pyautogui.press('tab') # apertar tab para ir para o campo da categoria

    # categoria
    categoria = str(tabela.loc[linha, 'categoria']) # pegar a categoria do produto da tabela
    pyautogui.write(categoria) # escrever a categoria do produto
    pyautogui.press('tab') # apertar tab para ir para o campo do preço unitário

    # preço unitário
    preco_unitario = str(tabela.loc[linha, 'preco_unitario']) # pegar o preço unitário do produto da tabela   
    pyautogui.write(preco_unitario) # escrever o preço unitário do produto 
    pyautogui.press('tab') # apertar tab para ir para o campo do custo

    # custo
    custo = str(tabela.loc[linha, 'custo']) # pegar o custo do produto da tabela
    pyautogui.write(custo) # escrever o custo do produto
    pyautogui.press('tab') # apertar tab para ir para o campo de observação

    # obs
    obs = str(tabela.loc[linha, 'obs']) # pegar a observação do produto da tabela
    if obs != 'nan': # se a observação não for vazia
        pyautogui.write(obs) # escrever a observação do produto
    pyautogui.press('tab') # apertar tab para ir para o botão de cadastrar
    
    pyautogui.press('enter') # apertar enter para cadastrar o produto
    
    # voltar para o início do formulário para cadastrar o próximo produto
    pyautogui.scroll(5000) # rolar a tela para cima (5000 é um valor grande para garantir que suba tudo)


# Passo 5: Repetir o passo 4 até acabar a lista de produtosMouse    2   19.95   5.0     


