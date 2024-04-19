

#INITIALISEER SPEL
GEHEIMWOORD = ["v","a","a","s"]
aantal_gokken = 0
lengteGeheimwoord = len( GEHEIMWOORD )
geraden_woord = lengteGeheimwoord * ["."]


#BEGIN TE SPELEN
while geraden_woord.count(".") > 0 and aantal_gokken < 10:

    gebruikers_gok = input("Typ je gok in: ")
    aantal_gokken += 1

    i = 0 #zet letter teller op 0
    while i < lengteGeheimwoord-1 :
         if gebruikers_gok == GEHEIMWOORD[i]:
           geraden_woord[i] = gebruikers_gok
           print("Goed gegokt!")
         i += 1 #verhoog teller

    print(geraden_woord)
    print("Je hebt nu", aantal_gokken, "keer geraden.")


#SPEL AFGELOPEN
print("Het spel is afgelopen.")
if geraden_woord.count(".") == 0:
    print("Je hebt gewonnen!")
elif aantal_gokken == 10:
    print("Je hebt verloren!")
