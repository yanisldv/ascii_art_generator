import pyfiglet

def list_all_fonts():
    return pyfiglet.FigletFont.getFonts()

def list_fonts():
    return list_all_fonts()[:10]

def generate_ascii_art(text, font='standard'):
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font)
        return ascii_art
    except pyfiglet.FontError:
        return "La police spécifiée n'est pas disponible."
    except Exception as e:
        if "caractère-non-géré" in str(e):
            return "Le caractère spécifié n'est pas pris en charge."
        else:
            raise e  # Relever l'exception si ce n'est pas lié à un caractère spécifique

if __name__ == "__main__":
    user_text = input("Entrez le texte pour l'art ASCII : ")
    
    # Liste toutes les polices disponibles
    print("Polices disponibles : ", ", ".join(list_all_fonts()))
    
    user_font = input("Entrez le nom de la police (appuyez sur Entrée pour la police par défaut) : ")
    result = generate_ascii_art(user_text, user_font if user_font else 'standard')
    print(result)
