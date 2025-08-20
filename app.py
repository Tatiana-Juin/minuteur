import customtkinter
from frame import MinuteurFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # apparence par defaut 
        customtkinter.set_appearance_mode("dark") 
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Minuteur")
        self.geometry("700x500")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.label_frame = MinuteurFrame(self)
        self.label_frame.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")
        
# LANCER L'APPLICATION
app =App()
app.mainloop()