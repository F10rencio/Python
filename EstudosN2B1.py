import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt


class Calculos:
    @staticmethod
    def calcular_pot_aparente(valor_tensao, valor_corrente):
        """Calcula a potência aparente (S) em VA."""
        return valor_tensao * valor_corrente

    @staticmethod
    def calcular_pot_ativa(valor_aparente, valor_fp):
        """Calcula a potência ativa (P) em W."""
        return valor_aparente * valor_fp

    @staticmethod
    def calcular_pot_reativa(valor_ativa, valor_aparente, tipo_carga="resistiva"):
        """Calcula a potência reativa (Q) em VAr."""

        valor = valor_aparente ** 2 - valor_ativa ** 2

        valor = max(0, valor)

        if tipo_carga == "indutiva":
            return sqrt(valor)

        elif tipo_carga == "capacitiva":
            return -sqrt(valor)

        else:
            return 0.0


class Aplicativo:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora de Potências Elétricas")
        self.janela.geometry("400x400")
        self.janela.resizable(False, False)

        ttk.Label(
            janela,
            text="Calculadora de Potências Elétricas",
            font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(
            janela,
            text="Entrada de Dados",
            font=("Arial", 10, "bold")).pack(
                anchor="w",
                padx=20,
                pady=5)

        ttk.Label(
            janela,
            text="Tensão [V]:").pack(
                anchor="w",
                padx=40,
                pady=2)

        self.entry_tensao = ttk.Entry(
            janela,
            width=20)

        self.entry_tensao.pack(
            padx=40,
            pady=2)

        ttk.Label(
            janela,
            text="Corrente [A]:").pack(
                anchor="w",
                padx=40,
                pady=2)

        self.entry_corrente = ttk.Entry(
            janela,
            width=20)

        self.entry_corrente.pack(
            padx=40,
            pady=2)

        ttk.Label(
            janela,
            text="Fator de Potência (fp ou cosφ):").pack(
                anchor="w",
                padx=40,
                pady=2)

        self.entry_fp = ttk.Entry(
            janela,
            width=20)

        self.entry_fp.pack(
            padx=40,
            pady=2)

        ttk.Label(
            janela,
            text="Tipo de carga:").pack(
                anchor="w",
                padx=40,
                pady=2)

        self.combo_carga = ttk.Combobox(
            janela,
            width=17,
            state="readonly",
            values=[
                "Resistiva",
                "Indutiva",
                "Capacitiva"
            ])

        self.combo_carga.pack(
            padx=40,
            pady=2)

        self.combo_carga.current(0)

        self.botao_calcular = ttk.Button(
            janela,
            text="Calcular",
            command=self.calcular)

        self.botao_calcular.pack(
            padx=20,
            pady=10,
            fill="x")

        ttk.Label(
            janela,
            text="Resultados",
            font=("Arial", 10, "bold")).pack(
                anchor="w",
                padx=20,
                pady=5)

        self.lbl_ativa = ttk.Label(
            janela,
            text="Potência ativa: -- W")

        self.lbl_ativa.pack(
            anchor="w",
            padx=40,
            pady=3)

        self.lbl_aparente = ttk.Label(
            janela,
            text="Potência aparente: -- VA")

        self.lbl_aparente.pack(
            anchor="w",
            padx=40,
            pady=3)

        self.lbl_reativa = ttk.Label(
            janela,
            text="Potência reativa: -- VAr")

        self.lbl_reativa.pack(
            anchor="w",
            padx=40,
            pady=3)

    def calcular(self):
        """Obtém os dados da interface e realiza os cálculos."""

        try:
            tensao = float(self.entry_tensao.get().replace(",", "."))
            corrente = float(self.entry_corrente.get().replace(",", "."))
            fp = float(self.entry_fp.get().replace(",", "."))

            if tensao < 0:
                raise ValueError("A tensão não pode ser negativa.")

            if corrente < 0:
                raise ValueError("A corrente não pode ser negativa.")

            if not 0 <= fp <= 1:
                raise ValueError(
                    "O fator de potência deve estar entre 0 e 1.")

            tipo_carga = self.combo_carga.get().lower()

            potencia_aparente = Calculos.calcular_pot_aparente(
                tensao,
                corrente)

            potencia_ativa = Calculos.calcular_pot_ativa(
                potencia_aparente,
                fp)

            potencia_reativa = Calculos.calcular_pot_reativa(
                potencia_ativa,
                potencia_aparente,
                tipo_carga)

            self.lbl_ativa.config(
                text=f"Potência ativa: {potencia_ativa:.2f} W")

            self.lbl_aparente.config(
                text=f"Potência aparente: {potencia_aparente:.2f} VA")

            self.lbl_reativa.config(
                text=f"Potência reativa: {abs(potencia_reativa):.2f} VAr")

        except ValueError as erro:
            messagebox.showerror(
                "Erro",
                str(erro))


if __name__ == "__main__":
    janela = tk.Tk()

    aplicativo = Aplicativo(janela)

    janela.mainloop()