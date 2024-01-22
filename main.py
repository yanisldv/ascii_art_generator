import pyfiglet

def generate_ascii_art(text):
    # Use the pyfiglet library to generate ASCII art
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    # Get user input for the text
    user_text = input("Enter the text for ASCII art: ")

    # Generate and display ASCII art
    result = generate_ascii_art(user_text)
    print(result)