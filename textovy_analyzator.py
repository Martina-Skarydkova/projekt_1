"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Martina Skarydkova
email: mskarydkova@gmail.com
"""

import string #lze také definovat ručně; string.punctuation by se nahradil punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
#uložené přihlašovací údaje
name = input("Zadej přihlašovací jméno:")
password = input("a přihlašovací heslo:")
user = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
set_cisel = [1, 2, 3]

# definované texty
text1 = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. '''

text2 = '''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.'''

text3 = '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''

texty = {1: text1, 2: text2, 3: text3}

def analyza_textu(texty):
    # odstranění interpunkce a příprava textu pro analýzu
    translator = str.maketrans('', '', string.punctuation)
    cisty_text = texty.translate(translator)
    words = []
    current_word = []
    
    for char in cisty_text:
        # Pokud je znak písmeno, přidám ho do slova
        if char.isalnum() or char == '-':
            current_word.append(char)
        # Pokud je to mezera nebo jiný znak, považuji aktuální slovo za ukončené
        elif current_word:
            words.append(''.join(current_word))  # Přidám aktuální slovo do seznamu
            current_word = []  # Vyprázdním aktuální slovo pro nové
    if current_word:
        words.append(''.join(current_word))  # Přidám poslední slovo, pokud nějaké je

    # Počet slov
    word_count = len(words)

    # Počet slov začínajících velkým písmenem
    capitalized_count = sum(1 for word in words if word[0].isupper())

    # Počet slov psaných velkými písmeny
    uppercase_count = sum(1 for word in words if word.isalpha() and word.isupper())

    # Počet slov psaných malými písmeny
    lowercase_count = sum(1 for word in words if word.islower())

    # Počet čísel (ne cifer)
    numbers = [word for word in words if word.isdigit()]
    number_count = len(numbers)

    # Suma všech čísel
    sum_numbers = sum(int(num) for num in numbers)

    # Vytisknutí výsledků
    print(f"Ve vybraném textu je {word_count} slov.")
    print(f"Ve vybraném textu je {capitalized_count} slov začínajících velkým písmenem.")
    print(f"Ve vybraném textu je {uppercase_count} slovo psané velými písmeny.")
    print(f"Ve vybraném textu je {lowercase_count} slov psaných malými písmeny.")
    print(f"Ve vybraném textu jsou {number_count} čísla (ne cifra):")
    print(f"Vybraný text má součet všech čísel {sum_numbers}")

    # Vytisknutí ve formátu dle zadání # nebo případně pevný print dle nejdelší vygenerované hodnoty ze všech textů  print("{:<3}|  {:<20}|{:>3}".format("LEN", "OCCURRENCES", "NR."))
    print("{:-<40}".format(""))  # Vytiskne oddělovač

    # Spočítání výskytu slov určité délky
    lengths = []
    counts = []
    # Zpracování každého slova
    for word in words:
        word_len = len(word)
        if word_len not in lengths:
            lengths.append(word_len)
            counts.append(1)
        else:
            index = lengths.index(word_len)
            counts[index] += 1

    # Seřazení podle délky slova (LEN) vzestupně
    sorted_lengths_counts = sorted(zip(lengths, counts))

    # Zjištění maximální délky výskytu
    max_occurrence_length = max(len("*" * count) for _, count in sorted_lengths_counts)

    # Dynamické přizpůsobení šířky sloupce "OCCURRENCES"
    header_format = "{:<3}|  {:<" + str(max_occurrence_length) + "}|{:>3}"
    row_format = "{:<3}| {:<" + str(max_occurrence_length) + "}|{:>3}"

    # Tisk hlavičky tabulky
    print(header_format.format("LEN", "OCCURRENCES", "NR."))
    print("{:-<40}".format(""))  # Vytiskne oddělovač

    # Iterace přes data a formátování řádků tabulky
    for length, count in sorted_lengths_counts:
        stars = "*" * count  # Vytvoření řetězce hvězdiček
        print(row_format.format(length, stars, count))

    print("{:-<40}".format(""))  # Vytiskne oddělovač

# ověření, že zadané údaje souhlasí
if user.get(name) == password:
    # pokud SOUHLASÍ, přivítej uživatele jménem
    print("{:-<40}".format(""))
    print("Ahoj", name, "vítej v aplikaci! Pokračuj na výběr textu.")
    print("Na výběr jsou 3 texty k analýze.")
    print("{:-<40}".format(""))
    try:
        cislo = int(input("Zadej číslo textového souboru od 1 do 3:"))
        print("Bylo zadané číslo:", cislo)
        print("{:-<40}".format(""))
        if cislo in set_cisel:
            vybrany_text = texty[cislo]  
            analyza_textu(vybrany_text)  # Zavolání funkce pro analýzu

        # Pokud uživatel vybere takové číslo textu nebo jiný vstup než číslo, které není v zadání, program jej upozorní a skončí
        else:
            print("Chyba, vybrali jste číslo, které není v nabídce. Program končí.")
    except ValueError:
        print("Chyba, zadané hodnota není číslo. Program končí.")
else:
    # Pokud uživatel není registrovaný, uveď zadané údaje, oznam nesprávné zadání a ukonči program.
    print("Zadané jméno:", name)
    print("Zadané heslo:", password)
    print("Uživatelské jméno nebo heslo nesouhlasí")