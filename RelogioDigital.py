from tkinter import *
from time import strftime


def att_relogio():
    horario_atual = strftime("%HH:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, att_relogio)


janela = Tk()
janela.title("Relógio Digital")

rotulo_relogio = Label(
    janela,
    font=("Arial", 200, "bold"),
    background="black",
    foreground="light green"
)

rotulo_relogio.pack(anchor="center")

att_relogio()

janela.mainloop()
