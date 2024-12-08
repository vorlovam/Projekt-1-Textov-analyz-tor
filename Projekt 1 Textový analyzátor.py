"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Markéta Vorlová
email: vorlovamarketa@seznam.cz
"""

# Registrovaní uživatelé
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení uživatele
username = input("Username: ")
password = input("Password: ")

# Ověření uživatele
if username in registered_users and registered_users[username] == password:
    print(f"Welcome to the app, {username}")
else:
    print("Unregistered user, terminating the program...")
    exit()

# Definice textů
TEXTS = [
    """Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet 
    above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, 
    which traverse the valley.""",
    
    """At the base of Fossil Butte are the bright red, 
    purple, yellow and gray beds of the Wasatch Formation. 
    Eroded portions of these horizontal beds slope gradually upward 
    from the valley floor and steepen abruptly.""",
    
    """The monument contains 8198 acres and protects a portion 
    of the largest deposit of freshwater fish fossils in the world. 
    The richest fossil fish deposits are found in multiple limestone layers, 
    which lie some 100 feet below the top of the butte."""
]

# Informace o dostupných textech
print("----------------------------------------")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("----------------------------------------")

# Výběr textu uživatelem
try:
    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice < 1 or text_choice > len(TEXTS):
        print("Invalid choice, terminating the program...")
        exit()
except ValueError:
    print("Invalid input, terminating the program...")
    exit()

# Vybraný text
selected_text = TEXTS[text_choice - 1]

# Rozdělení textu na jednotlivá slova
words = selected_text.split()

# Inicializace počítadel
word_count = len(words)
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numeric_sum = 0

# Analýza slov
for word in words:
    # Odstranění interpunkce na začátku a konci slova
    cleaned_word = word.strip(",.?!:;")

    # Kontrola typů slov
    if cleaned_word.istitle():  # Slovo začíná velkým písmenem
        titlecase_count += 1
    elif cleaned_word.isupper() and cleaned_word.isalpha():  # Velká písmena (bez čísel)
        uppercase_count += 1
    elif cleaned_word.islower():  # Malá písmena
        lowercase_count += 1
    elif cleaned_word.isdigit():  # Číselné řetězce
        numeric_count += 1
        numeric_sum += int(cleaned_word)

# Výsledky analýzy
print("----------------------------------------")
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers is {numeric_sum}.")
print("----------------------------------------")

# Slovník pro uložení délek slov a jejich počtu
word_lengths = {}

# Procházení všech slov a měření délky
for word in words:
    # Odstranění interpunkce z okrajů
    cleaned_word = word.strip(",.?!:;")
    length = len(cleaned_word)

    # Aktualizace počtu slov dané délky
    if length > 0:
        word_lengths[length] = word_lengths.get(length, 0) + 1

# Výstup délky slov v grafické podobě
print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
for length, count in sorted(word_lengths.items()):
    print(f"{length:>3}|{'*' * count:<13}|{count}")
