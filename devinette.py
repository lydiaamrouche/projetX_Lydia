print("Voici la devinette ")

nombre_secret = 23

while True:
    try:
        nombre_utilisateur = int(input("Tapez un nombre entre 0 et 100 : "))
        
        if 0 <= nombre_utilisateur <= 100:
            if nombre_utilisateur == nombre_secret:
                print("Gagné ")
                break
            else:
                print("Perdu  Essayez encore.")
        else:
            print("Le nombre doit être entre 0 et 100. Réessayez.")
    except ValueError:
        print("Entrée invalide. Veuillez taper un nombre.")
