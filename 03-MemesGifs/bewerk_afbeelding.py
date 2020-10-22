from PIL import Image
afbeelding = Image.open("baby_hulk.jpg")

# Afmetingen op het scherm zetten
# De breedte en hoogte van de afbeelding lezen en tonen 
breedte = afbeelding.width
hoogte = afbeelding.height	

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2

# Met str() zet je een int (getal) naar een string om. Dan kan print() het gebruiken.
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

# Andere info uitlezen en tonen
print(afbeelding.format, afbeelding.size, afbeelding.mode)

nieuwe_afmeting = (helft_breedte, helft_hoogte)
kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)
kleinere_afbeelding.save('baby_hulk_klein.jpg')


afbeelding = Image.open('baby_hulk_klein.jpg')
afbeelding.show()
breedte = afbeelding.width
hoogte = afbeelding.height	
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")