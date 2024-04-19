# DIT IS HET SPEL GALGJE
# GESCHREVEN DOOR ...
# Doel: het programma heeft een geheim woord,
# de gebruiker mag letter voor letter raden of die letter in het woord voorkomt
# het spel is afgelopen als de gebruiker het juiste woord geraden heeft of te veel fouten gemaakt heeft

#LET OP: dit programma is nog lang niet af.

###################
#GLOBALE VARIABELEN
####################
geheim_woord = ['h','a','l','l','o']	#dit is wat de gebruiker moet gaan raden
tot_nu_toe_geraden_woord = []					#dit is wat de gebruiker tot nu toe goed heeft geraden
resterende_pogingen = 8								#maximaal pogingen
spel_is_afgelopen = False						#als we beginnen is het spel nog niet afgelopen

##############
# DEFINITIES 
##############
def welkomstWoord():
	print("Welkom bij Galgje!")
	print("Dit zijn de spelregels ...")

# Deze functie vult de geraden woord aan met even veel streepjes als dat het gehiem woord lang is
def vulTotNuToeGeradenWoordMetStreepjes():
	for i in range(len(geheim_woord)):
		tot_nu_toe_geraden_woord.append("_")
		
def vervangStreepjeDoorLetterInGeradenWoord(gok):
	for i in range( len(geheim_woord)):
		if geheim_woord[i] == gok:
			print("letter zit erin!")
			tot_nu_toe_geraden_woord[i]=gok
	print("tot_nu_toe_geraden_woord", tot_nu_toe_geraden_woord)

def werkAantalPogingenBijAlsGokFout(gok):
	global resterende_pogingen #ik moet hier global gebruiken omdat ik een variabele van buiten de functie wil veranderen

	if not gok in geheim_woord:
		resterende_pogingen -= 1
	print("aantal resterende pogingen:", resterende_pogingen)


def controleerSpelIsAfgelopen():
	global spel_is_afgelopen

	print("waarde van spel is afgelopen", spel_is_afgelopen)
	if resterende_pogingen == 0:
		print("Jammer, te vaak fout gegokt. Je hebt verloren.") 
		spel_is_afgelopen = True
	elif geheim_woord == tot_nu_toe_geraden_woord:
		print("Jippie!! Je hebt het woord geraden, je hebt gewonnen!")
		spel_is_afgelopen = True

	if spel_is_afgelopen:
		print("Het spel is afgelopen!")


################
# HOOFDPROGRAMMA
################
welkomstWoord()
vulTotNuToeGeradenWoordMetStreepjes() #leeg woord aanvullen met juist aantal streepjes
print("pst… dit is het geheime_woord (wel zo makkelijk tijdens het testen):", geheim_woord) #even printen om te testen
print("tot_nu_toe_geraden_woord", tot_nu_toe_geraden_woord)
print("aantal resterende pogingen:", resterende_pogingen)


while not spel_is_afgelopen:
	gok = input ("Geef een letter: ")

	vervangStreepjeDoorLetterInGeradenWoord(gok) #vervangt _ door geraden letter
	werkAantalPogingenBijAlsGokFout(gok) #als fout geraden, dan aantal pogingen bijwerken
	controleerSpelIsAfgelopen()


# en dan komt hier de rest van het spel
# zolang spel niet is afgelopen, vragen om een gokletter
#		als gokletter er in voorkomt, dan feliciteren en voor elke voorkomen vervangen, en ...
#		als gokletter er niet in voorkomt, dan ...
# ...