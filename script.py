import csv

# Funkcija za proveru lakoće pamćenja brojeva
def kategorija_broja(broj):
    broj_str = str(broj).zfill(6)  # Dodavanje početnih nula za šestocifrene brojeve
    
    # Zlatna kategorija: vrlo lako pamtljivi brojevi
    if broj_str == broj_str[0] * 6:  # Ponavljanje iste cifre
        return "Zlatna"
    elif broj_str in ["123456", "234567", "345678", "456789", "987654", "876543", "765432", "654321"]:  # Sekvencijalni brojevi
        return "Zlatna"
    elif broj_str == broj_str[::-1]:  # Ogledalo simetrije
        return "Zlatna"
    
    # Srebrna kategorija: srednje lako pamtljivi brojevi
    elif broj_str[0:2] == broj_str[2:4] == broj_str[4:6]:  # Ponavljeni parovi cifara
        return "Srebrna"
    elif broj_str[::2] == broj_str[1::2]:  # Alternativni obrasci
        return "Srebrna"
    elif broj_str[:3] in ["123", "234", "345", "456", "567", "678", "789"] or broj_str[3:] in ["123", "234", "345", "456", "567", "678", "789"]:
        return "Srebrna"
    
    # Bronzana kategorija: teško pamtljivi brojevi
    else:
        return "Bronzana"

# Generisanje svih šestocifrenih brojeva i zapisivanje u CSV
with open("brojevi_kategorije.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Broj", "Kategorija"])
    
    for i in range(100000, 1000000):  # Brojevi od 100000 do 999999
        writer.writerow([i, kategorija_broja(i)])

print("Generisanje CSV fajla je završeno.")
