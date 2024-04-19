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

##############
# DEFINITIES 
##############
def welkomstWoord():
	print("Welkom bij Galgje!")
	print("Dit zijn de spelregels ...")

# Deze functie vult de geraden woord aan met even veel streepjes als dat het gehiem woord lang is
def vulTotNuToeGeradenWoordMetStreepjes():
	for i in range(len(geheim_woord)):				#voor elk letter in geheim woord
		tot_nu_toe_geraden_woord.append("_")		#per letter in het te raden woord aanvullen met streepjes
	print("tot_nu_toe_geraden_woord", tot_nu_toe_geraden_woord)	

# Deze functie verlaagt aantal pogingen bij een foute gok, anders aantal pogingen niet aanpassen
def werkAantalPogingenBijAlsGokFout(gok):
	global resterende_pogingen #ik moet hier global gebruiken omdat ik een variabele van buiten de functie wil veranderen
	if not gok in geheim_woord: #gok was fout
		resterende_pogingen -= 1
	print("aantal resterende pogingen:", resterende_pogingen) #even printen om te testen of het goed gaat



################
# HOOFDPROGRAMMA
################
welkomstWoord()
print("pst… dit is het geheime_woord (wel zo makkelijk tijdens het testen):", geheim_woord) #even printen om te testen
vulTotNuToeGeradenWoordMetStreepjes() #leeg woord aanvullen met juist aantal streepjes


#zolang het spel nog niet is afgelopen:
gok = input ("Geef een letter: ") 		#vraag om gokletter
werkAantalPogingenBijAlsGokFout(gok)  #als fout geraden, dan aantal pogingen bijwerken
# ...






