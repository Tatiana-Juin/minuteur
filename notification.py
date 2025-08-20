from plyer import notification

# METHODE POUR AFFICHER UNE NOTIFACATION 
def notify_user(title: str, message : str, duration: int = 5):
    notification.notify(
        title=title,
        message=message,
        timeout=duration  # durée d'affichage du pop up de fin 
    )