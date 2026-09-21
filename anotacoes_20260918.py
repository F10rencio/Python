import tkinter as tk
from tkinter import ttk, messagebox




class calculadora:
    def __init__(self, janela: tk.Tk):
        janela.geometry("500x400")
        #Esta ferramenta de texto não será editada e consultada posteriormente
        #Por isso ela já é declarada e montada em uma instrução
        ttk.Label(janela, text= "2º lei de Ohm",
                  font= ("Arial", 16, 'bold')).pack()
        
       
        self.lbl_combobox = ttk.Label(janela, text= "Escolha o material")
    

        #Declara um quadro para agrupar os radiobuttons
        self.frm_quadro1 = ttk.Frame(janela,
                                     relief= 'ridge'
                                     )

        #Declara o objeto que irá armazenar a escolha dos radiobuttons
        self.str_escolha = tk.StringVar(value= 'C')
        self.rdb_escolha1 = ttk.Radiobutton(self.frm_quadro1,
                                            text= "Cobre",
                                            variable= self.str_escolha,
                                            value= 'C')
        self.rdb_escolha2 = ttk.Radiobutton(self.frm_quadro1,
                                            text= "Alumínio",
                                            variable= self.str_escolha,
                                            value= 'A')
        self.rdb_escolha3 = ttk.Radiobutton(self.frm_quadro1,
                                            text= "Ouro",
                                            variable= self.str_escolha,
                                            value= 'O')
        self.btn_materiais = ttk.Button(self.frm_quadro1,
                                     text= 'Clique aqui', 
                                     command= self.acao_escolha_materiais)
        self.lbl_materiais = ttk.Label(self.frm_quadro1, text= 'Materiais')

        #Montagem
        self.lbl_combobox.pack()
        self.frm_quadro1.pack()
        self.rdb_escolha1.grid(row= 0, column= 0, padx= 3, pady= 3)
        self.rdb_escolha2.grid(row= 0, column= 1, padx= 3, pady= 3)
        self.rdb_escolha3.grid(row= 0, column= 2, padx= 3, pady= 3)
        self.btn_materiais.grid(row= 1,
                             column= 0,
                             columnspan= 4,
                             sticky= 'ew',
                             padx= 3, pady= 3)
        self.lbl_materiais.grid(row= 2,
                            column= 0,
                            columnspan= 4,
                            sticky= 'ew',
                            padx= 3, pady= 3)

    def acao_teste_escolha(self):
        self.btn_teste_escolha.config(text= self.cbb_escolhas.get())
        if self.cbb_escolhas.current() == 0:
            self.lbl_combobox.config(text= 'o cobre é um bom condutor de eletricidade!')
        elif self.cbb_escolhas.current() == 1:
            self.lbl_combobox.config(text= 'o alumínio é um excelente condutor de eletricidade!')
        elif self.cbb_escolhas.current() == 2:
            self.lbl_combobox.config(text= 'o ouro é um dos melhores condutores de eletricidade!')
        elif self.cbb_escolhas.current() == -1:
            self.lbl_combobox.config(text= 'Poxa meu, escolha uma das opções!')

    def acao_escolha_materiais(self):
        if self.str_escolha.get() == 'C':
            self.lbl_materiais.config(text= 'o cobre é um bom condutor de eletricidade!')
        elif self.str_escolha.get() == 'A':
            self.lbl_materiais.config(text= 'o alumínio é um excelente condutor de eletricidade!')
        elif self.str_escolha.get() == 'O':
            self.lbl_materiais.config(text= 'o ouro é um dos melhores condutores de eletricidade!')
if __name__ == "__main__":
    finestra = tk.Tk()
    calculadora(finestra)
    finestra.mainloop()