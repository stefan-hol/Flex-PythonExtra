from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("memerij.jpg")
tekengebied = ImageDraw.Draw(achtergrond)
breedte = achtergrond.width
hoogte = achtergrond.height	
lettertype = ImageFont.truetype("impact.ttf", 25)
tekst = "fuck it\nbaby hulk"
tekengebied.multiline_text((180,180), tekst, font=lettertype, fill=(255,255,255))

print("De achtergrond is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

achtergrond.show()
achtergrond.save("meme_met_tekst.jpg")