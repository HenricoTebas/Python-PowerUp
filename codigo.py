import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema
#abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

#Passo 2: Fezer login
pyautogui.click(x=781, y=406)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionar@gmail.com")

#passar para o campo da senha
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#Passo 3 - Pegar/importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

#Passo 4 - Cadastrar o produto
for linha in tabela.index:
    #codigo
    pyautogui.click(x=757, y=292)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    #clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)

#Passo 5:Repetir para todos os produtos