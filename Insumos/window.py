from tkinter import *
import tkinter.messagebox
from xml.sax.handler import EntityResolver
from matplotlib.pyplot import text
import pyodbc
import time
import pandas as pd


dados_conexao = ("Driver={SQL Server};"
                    "Server=DESKTOP-EC5CMDG;"
                    "Database=EstoqueLanchonete;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

def btn_clicked0(): #Lançar Insumo
    nome_insumo = entry0.get()
    data_validade = entry1.get()
    lote = entry2.get()
    quantidade = entry3.get()

    entry4.delete("1.0", 'end')
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde)
    VALUES
        ('{nome_insumo}', '{data_validade}', '{lote}', '{quantidade}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Adicionar Produto",message="Produto Adicionado com Sucesso")
    print("Adicionar Insumo")
    entry0.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')

def btn_clicked1(): #Procurar Insumo
    nome_insumo = entry0.get()
    print("Procurar Insumo")
    comando = f"""SELECT * from Insumos
            WHERE nome_insumo = '{nome_insumo}';
            """
    entry4.delete("1.0", 'end')
    cursor.execute(comando)
    for linha in cursor.fetchall():
        texto = f""" ----------------------------------\n Item: {linha.nome_insumo}\n Quantidade: {linha.qtde}\n Lote:{linha.lote}\n Validade:{linha.data_validade}\n"""
        entry4.insert("1.0", texto)

def btn_clicked2(): #Deletar Insumo
    nome_insumo = entry0.get()
    lote = entry2.get()
    comando = f"""SELECT * from Insumos
            WHERE nome_insumo = '{nome_insumo}'
            AND lote = {lote}
            """
    entry4.delete("1.0", 'end')
    cursor.execute(comando)
    for linha in cursor.fetchall():
        if nome_insumo == linha.nome_insumo:
            print('Deu Merda')
        else:
            texto = f""" ----------------------------------\n Item: {linha.nome_insumo}\n Lote:{linha.lote}"""
            entry4.insert("1.0", texto)

   
  


def btn_clicked3(): # Consumir Insumo
    nome_insumo = entry0.get()
    lote = entry2.get()
    qtde_usada = entry3.get()

    entry4.delete("1.0", 'end') 
    comando = f"""UPDATE Insumos
        SET qtde = qtde - {qtde_usada}
        WHERE nome_insumo = '{nome_insumo}'
        AND lote = {lote}
        """
    cursor.execute(comando)
    cursor.commit()
    print("Usar Insumo")
    tkinter.messagebox.showinfo(title="Aviso Uso Insumo",message=f"{qtde_usada} unidades do Produto: {nome_insumo} foram utilizadas")
    print("Button Saída de Insumo")
    entry0.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')

window = Tk()

window.geometry("703x739")
window.configure(bg = "#202122")
canvas = Canvas(
    window,
    bg = "#202122",
    height = 739,
    width = 703,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    350.5, 339.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    502.0, 275.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 367, y = 257,
    width = 270,
    height = 34)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    502.0, 331.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 367, y = 313,
    width = 270,
    height = 34)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    502.0, 388.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 367, y = 370,
    width = 270,
    height = 34)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    502.0, 447.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry3.place(
    x = 367, y = 429,
    width = 270,
    height = 34)

entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    502.0, 588.0,
    image = entry4_img)

entry4 = Text(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry4.place(
    x = 354, y = 485,
    width = 296,
    height = 204)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked0,
    relief = "flat")

b0.place(
    x = 25, y = 247,
    width = 180,
    height = 50)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b1.place(
    x = 25, y = 359,
    width = 180,
    height = 50)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b2.place(
    x = 25, y = 414,
    width = 180,
    height = 50)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b3.place(
    x = 25, y = 304,
    width = 180,
    height = 50)

window.resizable(False, False)
window.mainloop()
