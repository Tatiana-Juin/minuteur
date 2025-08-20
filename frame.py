import customtkinter


class MinuteurFrame (customtkinter.CTkFrame):
    def __init__(self,master):
        super().__init__(master)
        # VARIABLE POUR SAVOIR SI LE MINUTEUR EST LANCER, EN PAUSE,ET POUR GARDER L'IODENTIFIANT DU TIMER POUR L'ETAT DE PAUSE 
        self.visible_input = True;
        self.is_start = False
        self.is_paused = False
        self.id_timer = None

        # POUR APPELLER LES METHODES 
        from minuteur_methods import minuteur_methods
        minuteur_methods(self) 

        self.label_text=customtkinter.CTkLabel(self,text="Minuteur",font=("Arial",15))
        self.label_text.grid(row=0,column=0,padx=(0,10),pady=(10,0),sticky="n")
        # HEURE
        self.heure = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.label_heure=customtkinter.CTkLabel(self,text="h",font=("Arial",15))
        # MINUTE
        self.minute = customtkinter.CTkEntry(self,font=("Arial",12),text_color="white")
        self.label_minute=customtkinter.CTkLabel(self,text="m",font=("Arial",15))
        # ERREUR
        self.label_error = customtkinter.CTkLabel(self, font=("Arial",15),text_color="red",text="")
         # BTN
        self.btn = customtkinter.CTkButton(self,text="Démarrer",font=("Arial",15),command=self.toggle_input)
        # POUR AFFICHER UNE PREMIERE LES CHAMPS DE SAISIE DU TEMPS 
        self.show_input()
        # POUR APPELLER LE FICHIER CONTENANT TOUTE LES METHODE 
        minuteur_methods(self)