import tkinter as tk 
from tkinter import ttk
import math

class conversao:

    def __init__(self, janela):
        janela.title("Conversor de temperatura")
        janela.geometry("450x400")
        

        #Declaracao de Variaveis
        self.frm1 = ttk.LabelFrame(janela, text="Selecione a grandeza a ser aplicada", padding=15, borderwidth=5, relief="ridge")
        self.escolhardb = tk.StringVar(value="T")
        self.botTemperatura = ttk.Radiobutton(self.frm1, text="Temperatura [°C]", variable=self.escolhardb, value="T")
        self.botpressão = ttk.Radiobutton(self.frm1, text="Pressão [bar]", variable=self.escolhardb, value="P")
        self.botpotência = ttk.Radiobutton(self.frm1, text="Potência [kW]", variable=self.escolhardb, value="K")
       
        self.txtvalor = ttk.Entry(self.frm1, justify = "center")
        self.btncalcular = ttk.Button(self.frm1, text="Calcular", command=self.Calculos)
        self.lblResultado = ttk.Label(self.frm1, text="Resultado 1")
        self.lblResultado2 = ttk.Label(self.frm1, text="Resultado 2")
        self.btnfechar = ttk.Button(janela, text="Fechar", command=janela.destroy)

        #Montagem
        
        self.frm1.grid(row=0, column=0, columnspan=3, pady=15)
        self.botTemperatura.grid(row=0,column=0,padx=10,pady=5)
        self.botpressão.grid(row=0,column=1,padx=10,pady=5)
        self.botpotência.grid(row=0,column=2,padx=10,pady=5)
        self.txtvalor.grid(row=1, column=1, padx=10, pady=5)
        self.btncalcular.grid(row=2, column=1, padx = 10, pady=5)
        self.lblResultado.grid(row=4, column=0, pady=(0,15))
        self.lblResultado2.grid(row=5, column=0, pady=(0,15))
        self.btnfechar.grid(row=5, column=0, padx=25, pady=(0,15), sticky="e")

    def Calculos(self):
        try:
            # 1. Definir a resistividade (rho) do material (em Ohms.mm²/m)
            grandeza = self.escolhardb.get()

            valor = float(self.txtvalor.get().replace(",","."))

            if grandeza == "T": 
                tempF = ((valor * 1.8) + 32)
                kelvin = (valor + 273.15)

                self.lblResultado.config(text=f"resultado 1 = {tempF:.2f} F")
                self.lblResultado2.config(text=f"resultado 2 = {kelvin:.2f} K")
                
            elif grandeza == "P":  # pressão

                 Bar = valor*0.986923
                 Psi = valor*14.5038

                 self.lblResultado.config(text=f"resultado 1 = {Bar:.4f} F")
                 self.lblResultado2.config(text=f"resultado 2 = {Psi:.4f} K")

            elif grandeza == "K":  # potência

                 Cv = ((valor*1000)/736)
                 Hp = ((valor*1000)/746)

                 self.lblResultado.config(text=f"resultado 1 = {Cv:.2f} F")
                 self.lblResultado2.config(text=f"resultado 2 = {Hp:.2f} K")
                 

        except ValueError:
            # Captura o erro caso o usuário digite texto em vez de números, ou deixe em branco
            self.lblResultado.config(text="Erro: Digite um número válido na Medida.")

if __name__ == "__main__":
    janela = tk.Tk()
    conversao(janela)
    janela.mainloop()