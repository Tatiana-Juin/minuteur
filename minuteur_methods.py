from notification import notify_user
import customtkinter

def minuteur_methods(self):
    # METHODE POUR AFFICHER LES CHAMPS DE SAISIE UTILISATEUR 
    def show_input():

        
        self.heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))
        
        self.label_heure.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        # MINUTE
        
        self.minute.grid(row=1,column=2,padx=(0,10),pady=(10,0))
        
        self.label_minute.grid(row=1,column=3,padx=(0,10),pady=(10,0))

        # CREATION DU LABEL QUE L'ON APPELLE DANS LA FONCTION PLUS BAS POUR MODIFIER LE TEXTE PAR RAPPORT A CE QUE A ENTRER L'UTILISATEUR 
        
        # self.label_error.grid(row=2,column=0,padx=(0,10),pady=(10,0))
        self.label_error.grid(row=2, column=0, columnspan=6, pady=(10, 0), sticky="w")

        
        self.btn.grid(row=1,column=5,padx=(0,10),pady=(10,0))
    
    self.show_input = show_input
    
    # POUR LES VERIFICATION
    def verif():
            # recupere heure et minute  en chaine de caractere 
            heure = self.heure.get()
            minute = self.minute.get()
            # int_heure = int(heure) if heure else 0
            # pour verifier que les champs soit des nombre 
            if  (heure and not heure.isdigit()) or not minute.isdigit() or int(minute) > 59 or (int(minute) == 0 and heure =="") or ( int(minute) == 0 and  heure=="0"):
                self.label_error.configure(text="Erreur tu dois saisir un chiffre  ")
                self.heure.delete(0,'end')
                self.minute.delete(0,'end')
               
            else:
                # supprime le message d'erreur 
                self.label_error.configure(text="")
                # self.toggle_input()
                self.start()
    self.verif = verif
    
    #METHODE POUR  SWITCHER ENTRE PAUSE RESET ET LANCEMENT DU MINUTEUR   
    def toggle_input():

        if not self.is_start and not self.is_paused:
            self.verif()
        elif self.is_start and not self.is_paused:
            self.pause()
        elif self.is_paused:
            self.resume()
    self.toggle_input = toggle_input

    # METHODE POUR RECUPERER  LES MINUTES ,HEURE ET SECONDE ET CACHER LES ENTRER
    def start():
       
        # recupere les heure et minutes
        self.show_heure = self.heure.get()
        self.show_minute = self.minute.get()

        # cacher les entrer
        self.heure.grid_forget()
        self.label_heure.grid_forget()
        self.minute.grid_forget()
        self.label_minute.grid_forget()


        self.label_show_heure = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_heure.grid(row=1,column=0,padx=(0,10),pady=(10,0))

        self.label_show_minute = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_minute.grid(row=1,column=1,padx=(0,10),pady=(10,0))

        # POUR LES SECONDE 
        self.label_show_seconde  = customtkinter.CTkLabel(self,text="",font=("Arial",15))
        self.label_show_seconde.grid(row=1,column=2,padx=(0,10),pady=(10,0))

        self.conversion()

        self.is_start = True
        self.is_paused = False
        self.btn.configure(text="Pause")
    self.start = start

    # METHODE POUR LA CONVERSION POUR AFFICHER LES MINUTES ET HEURE
    def conversion():
        # Pour dire que le nombre est soit un nb  ou 0 
        heure_int = int(self.show_heure) if self.show_heure else 0
        minute_int = int(self.show_minute)
        self.total_seconde = (heure_int *3600) + (minute_int * 60)
        # POUR AFFICHER LE MINUTEUR 
        self.start_compt() 
    self.conversion = conversion

    # METHODE POUR AFFICHER LE MINUTEUR 
    def  start_compt():

        if self.total_seconde >= 0:
            # fait la conversion en minute 
            heures = self.total_seconde //3600
            minute_restante = (self.total_seconde % 3600) //60
            seconde = self.total_seconde % 60

            # POUR AFFICHER LE MINUTEUR 
            self.label_show_heure.configure(text=heures)
            self.label_show_minute.configure(text=minute_restante)
            self.label_show_seconde.configure(text=seconde)
            

            # Decrementer le compteur 
            self.total_seconde -=1;

            # Relance la fonction toute les secondes 
            self.id_timer = self.after(1000,self.start_compt)
            
        else:
            self.label_show_heure.configure(text="")

            self.label_show_minute.configure(text="")
            self.label_show_seconde.configure(text="Fin")

            # Texte ajouter
            self.is_start = False
            self.btn.grid_forget()
            self.reset()
            notify_user("Minuteur","Temps ecoulé")
    self.start_compt = start_compt

    # STOPER LE MINUTEUR 
    def stop_timer():
        if self.id_timer:
            self.after_cancel(self.id_timer)
            self.id_timer = None
    self.stop_timer = stop_timer

     # METHODE  POUR AFFICHER LE BOUTON RENITIALISER 
    def reset():
        self.btn_reset = customtkinter.CTkButton(self,text="Reset",font=("Arial",15),command=self.reset_timer)
        self.btn_reset.grid(row=1,column=6,padx=(0,10),pady=(10,0))
    self.reset = reset

    # METHODE POUR RENITIALISER LE TEMPS
    def reset_timer():
        self.stop_timer()
        self.show_input()
        self.label_show_heure.configure(text="")
        self.label_show_minute.configure(text="")
        self.label_show_seconde.configure(text="")
        self.heure.delete(0,'end')
        self.minute.delete(0,'end')
        self.btn.configure(text="Démarrer")
        #  sert a verifier si un objet btn reset possède un attribut donc existe 
        if hasattr(self,'btn_reset'):
            self.btn_reset.grid_forget()
            del self.btn_reset
        
        self.is_start = False
        self.is_paused=False
    self.reset_timer = reset_timer

    # METHODE POUR FAIRE LA PAUSE
    def pause():
        # RECUPERE ID 
        self.stop_timer()
        self.is_paused = True
        self.btn.configure(text="Relancer")
        self.reset()
    self.pause = pause

    # METHODE POUR RELANCER APRES LA PAUSE 
    def resume():
        self.is_paused = False
        self.start_compt()
        
        self.btn.configure(text="Pause")
    self.resume = resume
    