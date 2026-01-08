import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Captura os valores das entradas
        salario_bruto = float(entry_salario.get().replace(',', '.'))
        dias_vendidos = int(entry_dias.get())
        outros_proventos = float(entry_outros.get().replace(',', '.') or 0)

        if dias_vendidos > 10:
            messagebox.showwarning("Aviso", "Pela CLT, o limite de venda é de 1/3 das férias (geralmente 10 dias). Ajustando para 10.")
            dias_vendidos = 10
            entry_dias.delete(0, tk.END)
            entry_dias.insert(0, "10")

        # Lógica de cálculo
        base_calculo = salario_bruto + outros_proventos
        valor_dia = base_calculo / 30
        valor_abono = valor_dia * dias_vendidos
        terco_abono = valor_abono / 3
        total_venda = valor_abono + terco_abono

        # Atualiza os labels de resultado
        label_res_base.config(text=f"R$ {base_calculo:.2f}")
        label_res_abono.config(text=f"R$ {valor_abono:.2f}")
        label_res_terco.config(text=f"R$ {terco_abono:.2f}")
        label_res_total.config(text=f"R$ {total_venda:.2f}", fg="green", font=("Arial", 12, "bold"))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.\nUse ponto ou vírgula para decimais.")

# Configuração da Janela Principal
root = tk.Tk()
root.title("Calculadora de Venda de Férias")
root.geometry("400x450")
root.configure(padx=20, pady=20)

# Título
tk.Label(root, text="Calculadora de Férias", font=("Arial", 16, "bold")).pack(pady=10)

# Campos de Entrada
tk.Label(root, text="Salário Bruto (R$):").pack(anchor="w")
entry_salario = tk.Entry(root)
entry_salario.pack(fill="x", pady=5)

tk.Label(root, text="Dias a Vender (Abono):").pack(anchor="w")
entry_dias = tk.Entry(root)
entry_dias.pack(fill="x", pady=5)

tk.Label(root, text="Outros Proventos (R$):").pack(anchor="w")
entry_outros = tk.Entry(root)
entry_outros.insert(0, "0")
entry_outros.pack(fill="x", pady=5)

# Botão Calcular
btn_calcular = tk.Button(root, text="Calcular Venda", command=calcular, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=20, fill="x")

# Área de Resultados
frame_resultados = tk.LabelFrame(root, text=" Resultados ", padx=10, pady=10)
frame_resultados.pack(fill="both", expand=True)

tk.Label(frame_resultados, text="Base de Cálculo:").grid(row=0, column=0, sticky="w")
label_res_base = tk.Label(frame_resultados, text="R$ 0.00")
label_res_base.grid(row=0, column=1, sticky="e")

tk.Label(frame_resultados, text="Valor dos Dias:").grid(row=1, column=0, sticky="w")
label_res_abono = tk.Label(frame_resultados, text="R$ 0.00")
label_res_abono.grid(row=1, column=1, sticky="e")

tk.Label(frame_resultados, text="1/3 Constitucional:").grid(row=2, column=0, sticky="w")
label_res_terco = tk.Label(frame_resultados, text="R$ 0.00")
label_res_terco.grid(row=2, column=1, sticky="e")

tk.Label(frame_resultados, text="TOTAL A RECEBER:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=10)
label_res_total = tk.Label(frame_resultados, text="R$ 0.00", font=("Arial", 10, "bold"))
label_res_total.grid(row=3, column=1, sticky="e", pady=10)

# Rodapé informativo
tk.Label(root, text="*Cálculo referente apenas ao abono pecuniário.", font=("Arial", 8, "italic")).pack()

# Assinatura do Autor
tk.Label(root, text="Desenvolvido por: Higor Batista de Souza", font=("Arial", 9, "bold"), fg="#555").pack(pady=10)

root.mainloop()
