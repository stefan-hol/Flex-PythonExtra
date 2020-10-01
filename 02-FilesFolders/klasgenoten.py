import io
bestand = open("klasgenoten.txt", "w")
bestand.write("""jordan
""");
bestand.write("""guido
""");
bestand.write("""danny
""");
bestand.write("""thom
""");
bestand.write("""piter
""");
bestand.write("""mikey
""");
bestand.write("""becky
""");
bestand.write("""vincent
""");
bestand.write("""amy
""");
bestand.write("""yairme
""");
bestand.write("""bart
""");
bestand.close()

# Bestand in read-only (r) mode openen
bestand2 = open("klasgenoten.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print(inhoud)