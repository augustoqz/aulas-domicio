import os #Importa uma biblioteca
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageBrowserApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Navegador de Imagens") #Abre o navegador de imagens 
        
        self.image_paths= [] #Abre o caminho da imagem
        self.current_image_index = 0
        
        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)
        
        browser_button = tk.Button(root, text = "Selecionar Diretório", command=self.browse_directory) #Aqui ele abre uma pasta para selecionar um diretorio.
        browser_button.pack(padx=10, pady=5)
        
        self.prev_button = tk.Button(root, text="Anterior", state= tk.DISABLED, command=self.show_previous_image) #Aqui e um botão para voltar a uma imagem anterior.
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.next_button = tk.Button(root, text="Próxima", state=tk.DISABLED, command=self.show_next_image) #Aqui e um botão para ir para uma proxima imagem.
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=5)
        
        def browse_directory(self): #Abre o diretorio de pesquisa.
            directory_path = filedialog.askdirectory()
            if directory_path:
                self.image_paths = [
                    os.path.join(directory_path, file)
                    for file in os.listdir(directory_path)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) #Abre um LECK de tipos de imagens para selecionar.
                ]
                if self.image_paths:
                    self.current_image_index = 0
                    self.show_image(self.current_image_index)
                    self.next_button.config(state=tk.NORMAL)
                else:
                    self.image_label.config(text="Nenhuma Imagem Encontrada") #Avisa que não achou o tipo de imagem.

def show_image(self,index):
    image_path = self.image_paths[index]
    try:
        image = Image.open(image_path) #Abre a imagem.
        image = image.resize((300, 300))    #E o tamanho da imagem.
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
    except Exception as e:
        self.image_label.config(text=f"Erro ao abrir imagem: {str(e)}") #Mostra que deu um erro ao abrir a imagem
        
        def show_previous_image(self): #Volta para a imagem anterior
            if self.current_image_index > 0:
                self.current_image_index -= 1 #
                self.show_image(self.current_image_index)
                
        def show_next_image(self): #Troca a imagem para proxima
            if self.current_image_index < len(self.image_paths) -1:
                self.current_image_index += 1
                self.show_image(self.current_image_index)
                   
        if __name__ == "__main__": #Procura a imagem
            root = tk.Tk()
            app = ImageBrowserApp(root)
            root.mainloop() 
            
    

    

    

    
