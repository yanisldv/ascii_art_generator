import pyfiglet

def list_fonts():
    return pyfiglet.FigletFont.getFonts()

def generate_ascii_art(text, font='standard'):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except pyfiglet.FontError:
        return "La police spécifiée n'est pas disponible."

if __name__ == "__main__":
    user_text = input("Entrez le texte pour l'art ASCII : ")
    print("Polices disponibles : ", ", ".join(list_fonts()[:10]))  # Affiche seulement les 10 premières pour la simplicité
    user_font = input("Entrez le nom de la police (appuyez sur Entrée pour la police par défaut) : ")
    result = generate_ascii_art(user_text, user_font if user_font else 'standard')
    print(result)
