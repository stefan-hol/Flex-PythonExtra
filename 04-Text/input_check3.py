import re

while True:

    invoer = input("Voer je kenteken in: ")

    # Het klopt dat er een "r" voor de regular expression staat, zo voorkom je gedoe met speciale tekens
    patroon = r"\D{2}-? ?\d{3}-? ?\D{3}$"
    matches = re.findall(patroon, invoer)

    # Als we matches hebben voor de regular expression springen we uit de while
    if(len(matches) > 0):
        break

# Hier kom je pas uit als het telefoonnumer in het juiste formaat ingevoerd is.
print("Bedankt kenteken in juiste formaat:", matches[0])
