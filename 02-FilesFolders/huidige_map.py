#hier importeer ik os code denk ik en ik had geleik
import os

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)

# Op het scherm printen
print("De huidige map is: " + werkmap)

# Een nieuwe map maken met os.mkdir()


mapnaam = ""
lengte_mapnaam = 0

while lengte_mapnaam == 0:

	mapnaam = input("welke naam wil je voor de map ")

	lengte_mapnaam = len(mapnaam)


	if lengte_mapnaam > 0:
		os.mkdir(mapnaam)
		print("De map " + mapnaam + " is gemaakt.")

	else:
		print("Je hebt geen naam ingevoerd")