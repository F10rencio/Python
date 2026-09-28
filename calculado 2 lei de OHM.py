import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    def __init__(self, janela):
        janela.geometry("350x400")
        janela.title("Calculadora OHM")

# decdeclarar variaveis
        
        self.labtitulo = ttk.Label(janela, text = '2a Lei de OHM', font = ('Arial', 12)).grid(row = 0, column = 0, padx = 20, pady = 0)
        self.frm1 = ttk.LabelFrame(janela, text = 'Escolha o material', padding = 15, borderwidth = 5, relief = 'ridge')
        self.escolhabot = tk.StringVar(value = 'A')
        #escolha do material
        self.botaluminio = ttk.Radiobutton(self.frm1, text = 'Aluminio', variable = self.escolhabot, value = 'A')
        self.botcobre = ttk.Radiobutton(self.frm1, text = 'Cobre', variable = self.escolhabot, value = 'C')
        self.botaouro = ttk.Radiobutton(self.frm1, text = 'Ouro', variable = self.escolhabot, value = 'O')
        self.frm2 = ttk.LabelFrame(janela, text = 'Escolha a forma', padding = 15, borderwidth = 5, relief = 'ridge')
        self.perfil = ttk.Label(self.frm2, text = 'Perfil')
        self.cbbperfil = ttk.Combobox(self.frm2, values = ('Redondo', 'Triangular', 'Quadrado'))
        self.medida = ttk.Label(self.frm2, text = 'Medida em Metros')
        self.valmedida = ttk.Entry(self.frm2, justify = 'center')
        self.calcular = ttk.Button(janela, text = 'Calcular', command = self.Calculos)
        self.resultado = ttk.Label(janela, text = 'Resistencia Total: ..........Ohms')
        self.fechar = ttk.Button(janela, text = 'Fechar', command = janela.destroy)


    #montagem
        
        self.frm1.grid(padx = 5, pady = 5, ipadx = 0, ipady = 0)
        self.botaluminio.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.botcobre.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.botaouro.grid(row = 0, column = 2, padx = 10, pady = 5)
        self.frm2.grid(padx = 5, pady = 0, ipadx = 0, ipady = 0)
        self.perfil.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.cbbperfil.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.medida.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.valmedida.grid(row = 1, column = 1, padx = 10, pady = 5)
        self.calcular.grid(row=3,column=0,pady=(20,15))
        self.resultado.grid(row=4,column=0,pady=(0,15))
        self.fechar.grid(row=5,column=0,padx=25,pady=(0,15),sticky='e')

    def Calculos(self):
        try:
            # 1. Definir a resistividade (rho) do material (em Ohms.mm²/m)
            material = self.escolhabot.get()
            if material == 'C':    # Cobre
                rho = 0.0172
            elif material == 'A':  # Alumínio
                rho = 0.0282
            elif material == 'O':  # Ouro
                rho = 0.0244
            else:
                rho = 0.0172

            # 2. Capturar a medida digitada (trocando vírgula por ponto para evitar erro)
            medida = float(self.valmedida.get().replace(',', '.'))

            # 3. Calcular a área (A) da seção transversal baseado no perfil
            perfil = self.cbbperfil.get()
            if perfil == 'Redondo':
                area = math.pi * (medida ** 2) / 4
            elif perfil == 'Triangular':
                area = (math.sqrt(3) / 4) * (medida ** 2)
            elif perfil == 'Quadrado':
                area = medida ** 2
            else:
                area = medida ** 2

            # 4. Resistência: R = rho * (L / A) -> como o comprimento foi omitido,
            #    assumimos L = 1 m para obter a resistência unitária do material.
            resistencia = rho / area
            self.resultado.config(text = f'Resistencia Total: {resistencia:.4f} Ohms')
        except ValueError:
            self.resultado.config(text = 'Resistencia Total: Digite uma medida válida')
        except Exception:
            self.resultado.config(text = 'Resistencia Total: Erro de cálculo')


if __name__ == '__main__':
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()