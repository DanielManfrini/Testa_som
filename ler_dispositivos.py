import pyaudio
import tkinter as tk
import threading

from tkinter.ttk import Combobox 

p = pyaudio.PyAudio()

dispositivos = {}

dispositivos_de_entrada = {}
dispositivos_de_saida = {}

for i in range(p.get_host_api_info_by_index(0).get('deviceCount')):
    dispositivos = p.get_device_info_by_host_api_device_index(0, i)
    print(dispositivos)
    if dispositivos.get('maxInputChannels') > 0:
        dispositivos_de_entrada[i] = {
            'id' : i,
            'nome': dispositivos.get('name'), 
            'taxa': dispositivos.get('defaultSampleRate'), 
            'canais': dispositivos.get('maxInputChannels')
        }
    elif dispositivos.get('maxOutputChannels') > 0:
        dispositivos_de_saida[i] = {
            'id' : i,
            'nome': dispositivos.get('name'), 
            'taxa': dispositivos.get('defaultSampleRate'), 
            'canais': dispositivos.get('maxInputChannels')
        }
    else:
        pass

print(dispositivos_de_entrada)
print(dispositivos_de_saida)

nomes_de_entrada  = [nome['nome'] for nome in dispositivos_de_entrada.values()]
nomes_de_saida = [nome['nome'] for nome in dispositivos_de_saida.values()]

def janela_principal():

    def iniciar():
        botao_iniciar['state'] = tk.DISABLED
        botao_parar['state'] = tk.NORMAL
        
        def funcao():
            var['text'] = "0"

            if estado_equipamento_1.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_1_entrada.get()) :

                        entrada_1 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_1_saida.get()):

                        saida_1 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])
            
            if estado_equipamento_2.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_2_entrada.get()) :

                        entrada_2 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_2_saida.get()):

                        saida_2 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])
            
            if estado_equipamento_3.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_3_entrada.get()) :

                        entrada_3 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_3_saida.get()):

                        saida_3 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])
            
            if estado_equipamento_4.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_4_entrada.get()) :

                        entrada_4 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_4_saida.get()):

                        saida_4 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])
            
            if estado_equipamento_5.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_5_entrada.get()) :

                        entrada_5 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_5_saida.get()):

                        saida_5 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])
            
            if estado_equipamento_6.get() == True:

                for i in dispositivos_de_entrada.values():

                    if i['nome'] == str(equipamento_6_entrada.get()) :

                        entrada_6 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, input_device_index=i['id'])

                for i in dispositivos_de_saida.values():

                    if i['nome'] == str(equipamento_6_saida.get()):

                        saida_6 = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, output_device_index=i['id'])

            while var['text'] == "0":
                print("rodando")
                
                if estado_equipamento_1.get() == True:
                    audio_1 = entrada_1.read(1024)
                    saida_1.write(audio_1)
                
                if estado_equipamento_2.get() == True:
                    audio_2 = entrada_2.read(1024)
                    saida_2.write(audio_2)
            
                if estado_equipamento_3.get() == True:
                    audio_3 = entrada_3.read(1024)
                    saida_3.write(audio_3)

                if estado_equipamento_4.get() == True:
                    audio_4 = entrada_4.read(1024)
                    saida_4.write(audio_4)

                if estado_equipamento_5.get() == True:
                    audio_5 = entrada_5.read(1024)
                    saida_5.write(audio_5)

                if estado_equipamento_6.get() == True:
                    audio_6 = entrada_6.read(1024)
                    saida_6.write(audio_6)
            else:
                print("parou")
                return
        # criar uma nova thread de trabalho
        thread_iniciar = threading.Thread(target=funcao)

        # iniciar a thread
        thread_iniciar.start()

    def parar():
        var['text'] = "1"
        botao_iniciar['state'] = tk.NORMAL
        botao_parar['state'] = tk.DISABLED

    janela = tk.Tk()
    janela.title("Multi Tester")
    janela.resizable(0,0)
    janela.config(bg="white")

    janela.grid_columnconfigure(0, weight=1)
    janela.grid_rowconfigure(0, weight=1)
    fundo = tk.Frame(janela,bg="white",highlightthickness=1,highlightbackground='navy blue',padx=10, pady=10)
    fundo.grid(row=0, column=0, sticky="nsew")

    var = tk.Label(janela,text='0')

    # equipamento 1
    estado_equipamento_1 = tk.BooleanVar()
    fundo_equipamento_1 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_1.grid(column=0,row=1,padx=5,pady=5)
    tk.Label(fundo_equipamento_1,bg="white",text="Equipamento: 1").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_1 = tk.Checkbutton(fundo_equipamento_1,bg="white",text="Ativar equipamento",variable=estado_equipamento_1,onvalue=True,offvalue=False)
    check_equipamento_1.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_1,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_1_entrada = Combobox(fundo_equipamento_1, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_1_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_1,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_1_saida = Combobox(fundo_equipamento_1, width=30, state='readonly', values=nomes_de_saida)
    equipamento_1_saida.grid(column=1,row=3,padx=5,pady=5)

    # equipamento 2
    estado_equipamento_2 = tk.BooleanVar()
    fundo_equipamento_2 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_2.grid(column=1,row=1,padx=5,pady=5)

    tk.Label(fundo_equipamento_2,bg="white",text="Equipamento: 2").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_2 = tk.Checkbutton(fundo_equipamento_2,bg="white",text="Ativar equipamento",variable=estado_equipamento_2,onvalue=True,offvalue=False)
    check_equipamento_2.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_2,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_2_entrada = Combobox(fundo_equipamento_2, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_2_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_2,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_2_saida = Combobox(fundo_equipamento_2, width=30, state='readonly', values=nomes_de_saida)
    equipamento_2_saida.grid(column=1,row=3,padx=5,pady=5)

    # equipamento 3
    estado_equipamento_3 = tk.BooleanVar()
    fundo_equipamento_3 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_3.grid(column=2,row=1,padx=5,pady=5)

    tk.Label(fundo_equipamento_3,bg="white",text="Equipamento: 3").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_3 = tk.Checkbutton(fundo_equipamento_3,bg="white",text="Ativar equipamento",variable=estado_equipamento_3,onvalue=True,offvalue=False)
    check_equipamento_3.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_3,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_3_entrada = Combobox(fundo_equipamento_3, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_3_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_3,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_3_saida = Combobox(fundo_equipamento_3, width=30, state='readonly', values=nomes_de_saida)
    equipamento_3_saida.grid(column=1,row=3,padx=5,pady=5)

    # equipamento 4
    estado_equipamento_4 = tk.BooleanVar()
    fundo_equipamento_4 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_4.grid(column=0,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_4,bg="white",text="Equipamento: 4").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_4 = tk.Checkbutton(fundo_equipamento_4,bg="white",text="Ativar equipamento",variable=estado_equipamento_4,onvalue=True,offvalue=False)
    check_equipamento_4.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_4,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_4_entrada = Combobox(fundo_equipamento_4, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_4_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_4,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_4_saida = Combobox(fundo_equipamento_4, width=30, state='readonly', values=nomes_de_saida)
    equipamento_4_saida.grid(column=1,row=3,padx=5,pady=5)

    # equipamento 5
    estado_equipamento_5 = tk.BooleanVar()
    fundo_equipamento_5 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_5.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_5,bg="white",text="Equipamento: 5").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_5 = tk.Checkbutton(fundo_equipamento_5,bg="white",text="Ativar equipamento",variable=estado_equipamento_5,onvalue=True,offvalue=False)
    check_equipamento_5.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_5,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_5_entrada = Combobox(fundo_equipamento_5, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_5_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_5,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_5_saida = Combobox(fundo_equipamento_5, width=30, state='readonly', values=nomes_de_saida)
    equipamento_5_saida.grid(column=1,row=3,padx=5,pady=5)

    # equipamento 6
    estado_equipamento_6 = tk.BooleanVar()
    fundo_equipamento_6 = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=200,height=300)
    fundo_equipamento_6.grid(column=2,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_6,bg="white",text="Equipamento: 6").grid(column=0,row=0,columnspan=2,padx=5,pady=5)

    check_equipamento_6 = tk.Checkbutton(fundo_equipamento_6,bg="white",text="Ativar equipamento",variable=estado_equipamento_6,onvalue=True,offvalue=False)
    check_equipamento_6.grid(column=0,row=1,columnspan=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_6,bg="white",text="Entrada:").grid(column=0,row=2,padx=5,pady=5)
    equipamento_6_entrada = Combobox(fundo_equipamento_6, width=30, state='readonly', values=nomes_de_entrada )
    equipamento_6_entrada.grid(column=1,row=2,padx=5,pady=5)

    tk.Label(fundo_equipamento_6,bg="white",text="Saída:").grid(column=0,row=3,padx=5,pady=5)
    equipamento_6_saida = Combobox(fundo_equipamento_6, width=30, state='readonly', values=nomes_de_saida)
    equipamento_6_saida.grid(column=1,row=3,padx=5,pady=5)

    # RODAPÉ
    informacoes = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=274,height=50)
    informacoes.grid(column=0,row=3,padx=5,pady=5)

    tk.Label(informacoes,bg="white",text="Criado por: Daniel Lopes manfrini").place(x=5,y=5)
    tk.Label(informacoes,bg="white",text="Versão: 1.0").place(x=5,y=25)

    rodape = tk.Frame(fundo,bg="white",highlightthickness=1,highlightbackground='navy blue',width=558,height=50)
    rodape.grid(column=1,row=3,columnspan=2,padx=5,pady=5)

    botao_iniciar = tk.Button(rodape,text="Iniciar",command=iniciar,state=tk.NORMAL)
    botao_iniciar.place(x=450,y=10)

    botao_parar = tk.Button(rodape,text="Parar",command=parar,state=tk.DISABLED)
    botao_parar.place(x=500,y=10)

    janela.mainloop()

if __name__ == '__main__':
    
    inicia_janela = threading.Thread(target=janela_principal)

    inicia_janela.start()