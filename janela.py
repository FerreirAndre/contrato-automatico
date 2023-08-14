import tkinter as tk
import automacao
import functools

def submit():
  lista = []
  for entry in entry_list:
    lista.append(entry.get())
  automacao.substituicao(lista)

root = tk.Tk()
root.title("Dados para formação de contrato")

entry_list = []
dados = ['nome','cpf','rg','nascimento','rua','bairro', 'cidade','cep','estado','telefone','email','material','inicio','preço']
for i in range(14):
  label = tk.Label(root, text=f"{dados[i]}:")
  label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
  
  # text = tk.StringVar()
  entry = tk.Entry(root)
  entry.grid(row=i, column=1, padx=10, pady=5)
  entry_list.append(entry)

submit_button = tk.Button(root, text="Enviar", command=submit)
submit_button.grid(row=14, columnspan=2, pady=10)

root.mainloop()