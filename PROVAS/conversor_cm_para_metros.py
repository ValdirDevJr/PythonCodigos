import tkinter as tk

def converter_cm_para_metros():
    try:
        # Obter o valor em centímetros inserido pelo usuário
        valor_cm = float(entrada_cm.get())
        # Converter centímetros para metros
        valor_metros = valor_cm / 100
        # Atualizar o texto na label de resultado
        resultado_label.config(text=f'{valor_cm} centímetros é igual a {valor_metros:.2f} metros.')
    except ValueError:
        resultado_label.config(text='Por favor, insira um valor numérico válido.')

# Criar a janela principal
janela = tk.Tk()
janela.title('Conversor de Centímetros para Metros')

# Criar e posicionar os widgets
tk.Label(janela, text='Digite o valor em centímetros:').pack()
entrada_cm = tk.Entry(janela)
entrada_cm.pack()
tk.Button(janela, text='Converter', command=converter_cm_para_metros).pack()

resultado_label = tk.Label(janela, text='')
resultado_label.pack()

# Iniciar o loopda janela
janela.mainloop()
