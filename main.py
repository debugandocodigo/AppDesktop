import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp


class Application(tk.Tk):

    # Método construtor
    def __init__(self):
        super().__init__()

        self.title("Extrair Áudio de Vídeo") # Título da janela
        self.eval('tk::PlaceWindow . center') # Centralizar a janela
        self.geometry("400x200") # Tamanho da janela
        self.resizable(False, False) # Impedir redimensionamento

        # Adicionando um estilo de fonte para toda a aplicação
        self.fonte_padrao = ("Arial", 12)

        # Criando os widgets
        self.botao_selecionar = tk.Button(self,
                                          text="Selecionar Vídeo",
                                          font=self.fonte_padrao,
                                          command=self.selecionar_video)
        self.botao_selecionar.pack(pady=20)

        self.label_resultado = tk.Label(self, font=self.fonte_padrao, wraplength=350)
        self.label_resultado.pack(pady=10)

    # Método para selecionar um vídeo
    def selecionar_video(self):
        nome_arquivo_video = filedialog.askopenfilename(filetypes=[("Arquivos de vídeo", "*.mp4")])

        if nome_arquivo_video:
            nome_arquivo_audio = self.extrair_audio(nome_arquivo_video)

            if nome_arquivo_audio:
                self.label_resultado.config(text=f"Áudio extraído com sucesso: {nome_arquivo_audio}")
            else:
                self.label_resultado.config(text="Erro ao extrair áudio do vídeo.")

    # Método para extrair o áudio de um vídeo
    def extrair_audio(self, nome_arquivo_video):
        try:
            video = mp.VideoFileClip(nome_arquivo_video)
            nome_arquivo_audio = nome_arquivo_video.split('.')[0] + ".mp3"
            video.audio.write_audiofile(nome_arquivo_audio)

            return nome_arquivo_audio
        except Exception as e:
            return f"Erro ao extrair áudio: {e}"

    # Método para iniciar a aplicação
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
