import re
while True:

    invoer = input("Voer je postcode in: ")

    patroon = r"\d{4} ?\D{2}$"
    matches = re.findall(patroon, invoer)

    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt nummer in juiste formaat:", matches[0])
